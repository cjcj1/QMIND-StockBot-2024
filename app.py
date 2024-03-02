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
            dbc.Col(html.Img(src="/assets/8ball_icon.png", style={'width': '20%', 'height': '20%'}),
                    style={'textAlign': 'center'}, width=4)
        ])
    ]),
    html.Div([
        dbc.Row([
            dbc.Col(dcc.Input(value='tesla', id='stock_select'), style={'textAlign': 'center'}, width=4),
        ]),
    ]),
    html.Div([
        dcc.Loading(
            type='default',
            children=[
                html.Br(),
                dbc.Row([
                    html.H2(id='stock_pred', style={'color': 'white', 'textAlign': 'center'}),
                ]),
                html.Br(),
                dbc.Row([
                    html.H3("Score from -1 to 1:", style={'color': 'white', 'textAlign': 'center'}),
                    html.H3(id='stock_rating', style={'color': 'white', 'textAlign': 'center'}),
                ]),
            ]
        )
    ]),
    html.Div([
        html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
        html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
    ])
], style={'backgroundColor': 'black'}, fluid=True)


@app.callback(
    Output('stock_pred', 'children'), Output('stock_rating', 'children'),
    [Input('stock_select', 'value')]
)
def update_result(stock_select):
    stock_select = stock_select.replace(" ", "+")
    pred = live_nlp().run_nlp(stock_select)
    if stock_select == '' or stock_select == None:
        outlook = "not calculated"
    elif pred > 0:
        outlook = "GOOD"
    else:
        outlook = "BAD"
    return f"Outlook is {outlook}", round(pred, 3)


if __name__ == '__main__':
    app.run_server(debug=True)
