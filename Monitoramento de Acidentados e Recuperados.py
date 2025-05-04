import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import random

# Inicializando o app Dash
app = dash.Dash(__name__)
app.title = "Monitoramento de Estado de Pacientes"

# Layout do app
app.layout = html.Div([
    html.H1("Monitoramento de Acidentados e Recuperados", style={'textAlign': 'center', 'color': '#0074D9'}),

    dcc.Graph(id='grafico-pacientes'),

    dcc.Interval(
        id='intervalo-atualizacao',
        interval=2000,  # Atualiza a cada 2 segundos
        n_intervals=0
    ),

    html.Div(id='texto-status', style={'textAlign': 'center', 'fontSize': '22px', 'marginTop': '20px'})
])

# Callback para atualizar o gráfico e o texto dinamicamente
@app.callback(
    Output('grafico-pacientes', 'figure'),
    Output('texto-status', 'children'),
    Input('intervalo-atualizacao', 'n_intervals')
)
def atualizar_dados(n):
    acidentados = random.randint(10, 30)
    recuperados = random.randint(5, acidentados)  # Garantir que recuperados <= acidentados

    fig = go.Figure(data=[
        go.Bar(name='Acidentados', x=['Pacientes'], y=[acidentados], marker_color='red'),
        go.Bar(name='Recuperados', x=['Pacientes'], y=[recuperados], marker_color='green')
    ])
    
    fig.update_layout(
        barmode='group',
        title='Estado Atual dos Pacientes',
        yaxis=dict(title='Quantidade', range=[0, 35]),
        xaxis=dict(title='Categoria')
    )

    texto = f"Total de Acidentados: {acidentados} | Total de Recuperados: {recuperados}"
    return fig, texto

# Rodando o servidor local
if __name__ == '__main__':
    app.run(debug=True)
