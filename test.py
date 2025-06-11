from benchmark import Benchmark
import pandas as pd
from tqdm import tqdm
import os

# Configurações
algoritmos = ['hanoi']
entradas = [ 3, 6, 9, 13, 18, 23, 28, 33, 38, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]

entradas_curtas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12 ,13 ,14, 15, 16 , 17 ,18 ,19 ,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# Inicializar Benchmark
benchmark = Benchmark(
    bin_dir="./algoritmos"
)

# Coletar Resultados
resultados = []
os.makedirs("./resultados", exist_ok=True)
csv_path = "./resultados/resultados2.csv"

# Calcular total de iterações
total = len(algoritmos) * len(entradas)

# Loop com Barra de Progresso
print("Iniciando Benchmark...")
with tqdm(total=total, desc="Benchmark Progress", unit="test") as pbar:
    for algoritmo in algoritmos:
        for entrada in entradas:
            #print(f" Executando {algoritmo} com {entrada}")
            resultado = benchmark.run_test(
                algoritmo=algoritmo,
                entrada=entrada,
            )
            if resultado:
                resultados.append(resultado)
                df = pd.DataFrame(resultados)
                # Converter colunas numéricas para float
                colunas_numericas = [
                    "tempo_execucao_medio_s",
                    "memoria_media_MB",
                    "memoria_maxima_media_MB",
                    "memoria_minima_media_MB",
                    "cpu_media_percent",
                    "tamanho_entrada"
                ]
                for coluna in colunas_numericas:
                    if coluna in df.columns:
                        df[coluna] = pd.to_numeric(df[coluna], errors="coerce")
                df.to_csv(csv_path, index=False)
            pbar.update(1)

print("Benchmark concluído!")
print(f" CSV salvo em {csv_path}")
