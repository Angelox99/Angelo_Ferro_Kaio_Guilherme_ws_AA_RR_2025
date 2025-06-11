import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# ==============================
# Leitura dos Dados
# ==============================

df_arm = pd.read_csv("./resultados/resultados(arm).csv")
# df_x86 = pd.read_csv("./resultados/resultados(x86).csv")

df_arm["processador"] = "arm(M1)"
#df_x86["processador"] = "x86(i7-14700KF)"

#df = pd.concat([df_arm, df_x86], ignore_index=True)
df = df_arm.copy()

# converte a Coluna de tempo de execução de segundos para min

def converter_tempo_execucao(df):
    df["tempo_execucao_medio_s"] = pd.to_numeric(df["tempo_execucao_medio_s"], errors="coerce")
    df["tempo_execucao_medio_min"] = df["tempo_execucao_medio_s"] / 60
    return df

df = converter_tempo_execucao(df)

# pega so os 10 primeiros resultados
# df = df[df["tamanho_entrada"] <= 33]

# ==============================
# Função para gerar gráficos
# ==============================

def gerar_grafico(metric):
    df_filtrado = df[df["algoritmo"] == "hanoi"].copy()
    df_filtrado[metric] = pd.to_numeric(df_filtrado[metric], errors="coerce")
    df_filtrado["algoritmo_proc"] = df_filtrado["algoritmo"] + " (" + df_filtrado["processador"] + ")"
    df_filtrado = df_filtrado.sort_values(by="tamanho_entrada")
    fig = px.line(
        df_filtrado,
        x="tamanho_entrada",
        y=metric,
        color="algoritmo_proc",
        markers=True,
        title=f"{metric} - Hanoi",
        labels={
            "tamanho_entrada": "Tamanho da Entrada",
            metric: f"{metric}",
            "algoritmo_proc": "Algoritmo (Processador)"
        }
    )
    fig.update_layout(
        template="plotly_white",
        width=1200,
        height=500,
        title_x=0.5
    )
    return fig

# ==============================
# App Dash
# ==============================

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Dashboard Benchmark Hanoi"

app.layout = dbc.Container([
    html.H1("Benchmark - Algoritmo de Hanoi", className="text-center my-4"),
    dbc.Tabs([
        dbc.Tab(label="Hanoi", children=[
            dcc.Graph(id="grafico-tempo"),
            dcc.Graph(id="grafico-cpu"),
            dcc.Graph(id="grafico-memoria"),
        ]),
    ])
], fluid=True)

# ==============================
# Callbacks para atualizar os gráficos
# ==============================

@app.callback(
    Output("grafico-tempo", "figure"),
    Output("grafico-cpu", "figure"),
    Output("grafico-memoria", "figure"),
    Input("grafico-tempo", "id")
)
def atualizar_graficos(_):
    fig_tempo = gerar_grafico("tempo_execucao_medio_min")
    fig_cpu = gerar_grafico("cpu_media_percent")
    fig_memoria = gerar_grafico("memoria_media_MB")
    return fig_tempo, fig_cpu, fig_memoria

# ==============================
# Executar App
# ==============================

if __name__ == "__main__":
    app.run(debug=True)