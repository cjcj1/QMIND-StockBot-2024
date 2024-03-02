import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
from live_demo import live_nlp

app = dash.Dash(__name__)

app.layout = dbc.Container([
    html.Div([
        html.Br(),
        html.H1(children='Ask The Magic 8 Ball to Forecast a Stock',
                style={'color': 'white', 'textAlign': 'center'}),
        html.Br()
    ]),
    html.Div([
        dbc.Row([
            dbc.Col(width=5),
            dbc.Col(html.Img(src="/assets/8ball_icon.png", style={'width': '20%', 'height': '20%'}),
                    style={'textAlign': 'center'}, width=4)
        ])
    ]),
    html.Div([
        dbc.Row([
            dbc.Col(width=4),
            dbc.Col(dcc.Input(value='tesla', id='stock_select'), width=4),
        ]),
    ]),
    html.Div([
        dcc.Loading(
            type='default',
            children=[
                html.Br(),
                html.H2(id='stock_pred', style={'color': 'white', 'textAlign': 'center'})
            ]
        )
    ]),
    html.Div([
        html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
        html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
    ])
], style={'backgroundColor': 'black'}, fluid=True)


@app.callback(
    Output('stock_pred', 'children'),
    [Input('stock_select', 'value')]
)
def update_result(stock_select):
    pred = live_nlp().run_nlp(stock_select)
    if pred > 0:
        outlook = "GOOD"
    else:
        outlook = "BAD"
    return f"Outlook is {outlook}"


if __name__ == '__main__':
    app.run_server(debug=True)
