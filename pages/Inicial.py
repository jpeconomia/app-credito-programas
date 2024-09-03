

import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H2('Crédito Rural e Produtos Florestais'),
    html.P('Este aplicativo apresenta os dados de crédito acessado vinculado a programas de política pública.'),
    html.P('Foram escolhidas linhas que, em sua descrição, apresentam alguma finalidade voltada para atividades florestais.'),
    html.P('Os dados foram extraídos dos dados abertos da API do SICOR (Sistema de Operações do Crédito Rural e do Proagro)')
])

