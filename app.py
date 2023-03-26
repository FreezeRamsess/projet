import requests
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

# récupération des données depuis l'URL
url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=binancecoin'
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)

# création de l'application Dash
app = dash.Dash(__name__)

# création du graphique
fig = {
    'data': [
        {'x': df['last_updated'], 'y': df['current_price'], 'type': 'line', 'name': 'BNB Price'},
    ],
    'layout': {
        'title': 'Binance Coin (BNB) Price',
        'xaxis': {'title': 'Date'},
        'yaxis': {'title': 'Price (USD)'}
    }
}

# affichage du graphique sur le dashboard
app.layout = html.Div(children=[
    html.H1(children='Binance Coin (BNB) Price'),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)