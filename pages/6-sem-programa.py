import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd 

dash.register_page(__name__, name = '6. Sem Programa')

df = pd.read_csv('https://drive.google.com/uc?export=download&id=1_Q4I9iLjxMnRqLzcOAPfTSGsN8F3kRBE')

df2 = df.loc[df['cdSubPrograma'] == 'Sem Subprograma']

layout = html.Div([

    html.H2('6: Crédito Acessado Sem Vínculo a Programa'),

    html.H2('Gráfico 6.1: Evolução por Estado'),
    
    dcc.Dropdown(id = 'dropdown-grafico-6-1',
                 options = sorted(df2['nomeUF'].unique()),
                 value = 'Bahia',
                 multi = True),
    
    dcc.Graph(id = 'grafico-6-1'),

    html.H2('Gráfico 6.2: Ano Safra, Estado e Produtos'),

    html.P('Ano Safra'),

    dcc.Dropdown(id = 'ano-safra-grafico-6-2',
                 options = sorted(df2['Ano Safra'].unique()),
                 value = '2022/23'),

    html.P('Unidade Federativa'),

    dcc.Dropdown(id = 'uf-grafico-6-2',
                 options = sorted(df2['nomeUF'].unique()),
                 value = ['Acre','Bahia'],
                 multi = True),

    html.P('Produtos'),

    dcc.Dropdown(id = 'produtos-grafico-6-2',
                 options = ['Abacate'],
                 value = 'Florestamento E Reflorestamento',
                 multi = True),

    dcc.Graph(id = 'grafico-6-2'),

    html.H2('Gráfico 6.3: Ano Safra, Estado e Fontes de Recurso'),

    html.P('Ano Safra'),

    dcc.Dropdown(id = 'ano-safra-grafico-6-3',
                 options = sorted(df2['Ano Safra'].unique()),
                 value = '2022/23'),

    html.P('Unidade Federativa'),

    dcc.Dropdown(id = 'uf-grafico-6-3',
                 options = ['Bahia','Amapá'],
                 value = 'Bahia'),

    dcc.Graph(id = 'grafico-6-3'),
    
    html.H2('Gráfico 6.4: Brasil como um todo'),

    html.P('Ano Safra'),

    dcc.Dropdown(id = 'ano-safra-grafico-6-4',
                 options = sorted(df2['Ano Safra'].unique()),
                 value = '2022/23'),

    dcc.Graph(id = 'grafico-6-4')

])

@callback(
    Output('grafico-6-1','figure'),
    Input('dropdown-grafico-6-1','value')
)

def grafico_6_1(UF):
    
    a = df2[['Ano Safra','VlInvestimento','nomeUF']].groupby(['Ano Safra','nomeUF'], as_index = False).sum()

    a = a.pivot(index = 'Ano Safra',columns = 'nomeUF', values = 'VlInvestimento').fillna(0).reset_index()

    fig = px.bar(a, 
                 'Ano Safra',
                 UF,
                 labels = {'VlInvestimento':'Investimento',
                           'variable':'UF',
                           'value':'R$'},
                 title = f'Investimento')

    return fig

@callback(
    Output('produtos-grafico-6-2','options'),
    Input('ano-safra-grafico-6-2','value'),
    Input('uf-grafico-6-2','value')
)

def prods_grafico_6_2(ano,ufs): 

    a = df2[df2['Ano Safra'] == ano]

    a = a[a['nomeUF'].isin(ufs)]

    options = sorted(a['nomeProduto'].unique())

    return [i for i in options]


@callback(
    Output('grafico-6-2','figure'),
    Input('ano-safra-grafico-6-2','value'),
    Input('uf-grafico-6-2','value'),
    Input('produtos-grafico-6-2','value')
)

def grafico_6_2(ano,ufs,prods): 

    a = df2.loc[df['Ano Safra'] == ano]

    a = a.loc[a['nomeUF'].isin(ufs)]

    a = a[['nomeUF','nomeProduto','VlInvestimento']].groupby(['nomeUF','nomeProduto'], as_index = False).sum()

    a = a.pivot(index = 'nomeUF', columns = 'nomeProduto', values = 'VlInvestimento').fillna(0).reset_index()

    fig = px.bar(a,
                 'nomeUF',
                 prods, 
                 labels = {'value':'R$',
                          'variable':'Produtos',
                          'nomeUF':'Unidades Federativas'})
    

    return fig


@callback(
    Output('uf-grafico-6-3','options'),
    Input('ano-safra-grafico-6-3','value')
)

def ufs_grafico_6_3(ano): 

    a = df2.loc[df2['Ano Safra'] == ano]

    options = sorted(a['nomeUF'].unique())

    return options

@callback(
    Output('grafico-6-3','figure'),
    Input('ano-safra-grafico-6-3','value'),
    Input('uf-grafico-6-3','value')
)

def grafico_6_3(ano,uf): 

    a = df2.loc[(df2['Ano Safra'] == ano) & (df2['nomeUF'] == uf)]

    a = a[['VlInvestimento','nomeProduto','cdFonteRecurso']].groupby(['nomeProduto','cdFonteRecurso'], as_index = False).sum()

    a = a.pivot(index = 'nomeProduto', columns = 'cdFonteRecurso', values = 'VlInvestimento').fillna(0).reset_index()

    fig = px.bar(a,
                 [i for i in a.columns if i != 'nomeProduto'],
                 'nomeProduto',
                 labels = {'variable':'Fonte',
                           'value':'R$',
                           'nomeProduto':'Produto'})
    
    return fig
    
   
@callback(
    Output('grafico-6-4','figure'),
    Input('ano-safra-grafico-6-4','value')
)

def grafico_6_4(ano): 

    a = df2.loc[df2['Ano Safra'] == ano]

    a = a[['VlInvestimento','nomeProduto','cdFonteRecurso']].groupby(['nomeProduto','cdFonteRecurso'], as_index = False).sum()

    a = a.pivot(index = 'nomeProduto', columns = 'cdFonteRecurso', values = 'VlInvestimento').fillna(0).reset_index()

    fig = px.bar(a,
           [i for i in a.columns if i != 'nomeProduto'],
           'nomeProduto',
           labels = {'variable':'Fonte',
                     'value':'R$',
                     'nomeProduto':'Produto'})
    
    return fig


