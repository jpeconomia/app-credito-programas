import dash
from dash import Dash, html, dcc
import pandas as pd 
import dash_bootstrap_components as dbc
# from dash_bootstrap_templates import load_figure_template

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

df = pd.read_csv('https://drive.google.com/uc?export=download&id=1_Q4I9iLjxMnRqLzcOAPfTSGsN8F3kRBE')

app = Dash(__name__, use_pages=True,external_stylesheets = [dbc.themes.CYBORG, dbc_css])
# load_figure_template('CYBORG')

app.layout = html.Div([
    html.H1('Crédito acessado por programas de política pública'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug = True, port = 8090)

