#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void hanoi(int n, char origem, char destino, char auxiliar) {
    if (n > 0) {
        hanoi(n - 1, origem, auxiliar, destino);
        //printf("Move o disco %d de %c para %c\n", n, origem, destino);
        hanoi(n - 1, auxiliar, destino, origem);
    }
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
    hanoi(n, 'A', 'C', 'B');
    clock_t fim = clock();
    double tempo = (double)(fim - inicio) / CLOCKS_PER_SEC;
    printf("Tempo de execucao: %.6f segundos\n", tempo);

    return 0;
}