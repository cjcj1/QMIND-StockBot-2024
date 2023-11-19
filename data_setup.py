import pandas as pd
import yfinance as yf
import requests
from bs4 import BeautifulSoup

response = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
tickers = soup.find_all('table')[0]
stocks = pd.read_html(str(tickers))[0]
stocks = stocks.dropna(axis=1)

df = yf.download(stocks.Symbol.to_list(), start="2020-11-01", end="2023-10-30")
df = df.dropna(axis=1)
df_open = df["Open"]
df_high = df["High"]
df_low = df["Low"]
df_close = df["Close"]
df_adj_close = df["Adj Close"]
df_vol = df["Volume"]
print(df_open.to_string())
df_adj_close.to_csv('Stocks_AdjClose_3yr.csv')
df_vol.to_csv('Stocks_Volume_3yr.csv')
