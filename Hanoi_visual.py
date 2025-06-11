import os
import time

def desenhar_torres(torres, n):
    os.system('clear')  # Limpa o terminal no macOS/Linux
    largura_max = n * 2 - 1
    for nivel in range(n-1, -1, -1):
        for t in 'ABC':
            if len(torres[t]) > nivel:
                disco = torres[t][nivel]
                largura = disco * 2 - 1
                espacos = (largura_max - largura) // 2
                print(' ' * espacos + '#' * largura + ' ' * espacos, end=' ')
            else:
                print(' ' * largura_max, end=' ')
        print()
    print('-' * (largura_max * 3 + 2))
    print('   A' + ' ' * (largura_max-2) + 'B' + ' ' * (largura_max-2) + 'C\n')
    time.sleep(0.3)

def hanoi(n, origem, destino, auxiliar, torres, total):
    if n > 0:
        hanoi(n-1, origem, auxiliar, destino, torres, total)
        disco = torres[origem].pop()
        torres[destino].append(disco)
        desenhar_torres(torres, total)
        hanoi(n-1, auxiliar, destino, origem, torres, total)

def main():
    n = 30
    torres = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    desenhar_torres(torres, n)
    hanoi(n, 'A', 'C', 'B', torres, n)

if __name__ == '__main__':
    main()