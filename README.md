## Como Executar o Projeto

Siga os passos abaixo para rodar os benchmarks e visualizar os resultados:

### 1. Compilar os Algoritmos em C

Entre na pasta `algoritmos` e execute o comando para gerar o executável:

```sh
cd algoritmos
make
cd ..
```

### 2. Instalar os Requisitos do Python

Na pasta raiz do projeto, instale as dependências necessárias:

```sh
pip install -r requirements.txt
```

### 3. Executar os Testes de Benchmark

Rode o script de testes para coletar os resultados:

```sh
python test.py
```

Os resultados serão salvos na pasta `resultados`.

### 4. Visualizar os Gráficos

Execute o script para abrir o dashboard com os gráficos:

```sh
python grafico.py
```

Acesse o endereço exibido no terminal para visualizar os resultados no navegador.

---

**Observação:**  
Certifique-se de ter o `make` e um compilador C instalados no sistema, além do Python 3.