#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>

#define MAX_DEPTH 3

typedef struct {
    int n;
    char origem;
    char destino;
    char auxiliar;
    int depth;
} hanoi_args;

void* hanoi_parallel(void* args);

void hanoi(int n, char origem, char destino, char auxiliar, int depth) {
    if (n > 0) {
        if (depth < MAX_DEPTH) {
            pthread_t t1, t2;
            hanoi_args args1 = {n - 1, origem, auxiliar, destino, depth + 1};
            hanoi_args args2 = {n - 1, auxiliar, destino, origem, depth + 1};
            pthread_create(&t1, NULL, hanoi_parallel, &args1);
            pthread_create(&t2, NULL, hanoi_parallel, &args2);
            pthread_join(t1, NULL);
            pthread_join(t2, NULL);
        } else {
            hanoi(n - 1, origem, auxiliar, destino, depth + 1);
            hanoi(n - 1, auxiliar, destino, origem, depth + 1);
        }
    }
}

void* hanoi_parallel(void* args) {
    hanoi_args* h = (hanoi_args*)args;
    hanoi(h->n, h->origem, h->destino, h->auxiliar, h->depth);
    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Uso: %s <numero_de_discos>\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);
    if (n <= 0) {
        printf("Numero de discos invalido.\n");
        return 1;
    }

    clock_t inicio = clock();
    hanoi(n, 'A', 'C', 'B', 0);
    clock_t fim = clock();
    double tempo = (double)(fim - inicio) / CLOCKS_PER_SEC;
    printf("Tempo de execucao: %.6f segundos\n", tempo);

    return 0;
}