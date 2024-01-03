import pandas as pd
import yfinance as yf
import requests
from bs4 import BeautifulSoup
from io import StringIO

response = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
tickers = soup.find_all('table')[0]
stocks = pd.read_html(StringIO(str(tickers)))[0]
stocks = stocks.dropna(axis=1)

df = yf.download(stocks.Symbol.to_list(), start="2014-01-01", end="2023-12-31")
df = df.dropna(axis=1)
df.index = pd.to_datetime(df.index.get_level_values(0))
df.index = df.index.date
adj = df["Adj Close"]
vol = df["Volume"]
adj.to_csv('Stocks_AdjClose_10yr.csv')
vol.to_csv('Stocks_Volume_10yr.csv')

divs_list = []
divs = pd.DataFrame()

for ticker_symbol in stocks.Symbol:
    stock_divs = yf.Ticker(ticker_symbol).dividends
    stock_divs = pd.Series(stock_divs)
    stock_divs = stock_divs.loc["2014-01-01":"2023-12-31"]
    if len(stock_divs) > 0:
        divs_list.append(stock_divs.rename(ticker_symbol))

divs = pd.concat(divs_list, axis=1)

divs = divs.dropna(how='all')
new_divs = pd.DataFrame()
new_divs["placeholder"] = adj["A"]
new_divs["placeholder"].values[:] = 0
divs = pd.concat([new_divs, divs])
divs = divs.dropna(how='all')

divs = divs.drop(columns=["placeholder"])
divs = divs.reindex(sorted(divs.columns), axis=1)


def update_early_cells_divs(column):
    first_non_na = column.first_valid_index()
    if first_non_na is not None:
        divs.loc[:first_non_na, column.name] = column[first_non_na]


divs.apply(update_early_cells_divs, axis=0)

divs = divs.fillna(method='ffill')

divs.to_csv('Stocks_Dividends_10yr.csv')

splits_list = []
splits = pd.DataFrame()

for ticker_symbol in stocks.Symbol:
    stock_splits = yf.Ticker(ticker_symbol).splits
    stock_splits = pd.Series(stock_splits)
    stock_splits = stock_splits.loc["2014-01-01":"2023-12-31"]
    if len(stock_splits) > 0:
        splits_list.append(stock_splits.rename(ticker_symbol))

splits = pd.concat(splits_list, axis=1)

splits = splits.dropna(how='all')
new_splits = pd.DataFrame()
new_splits["placeholder2"] = adj["A"]
new_splits["placeholder2"].values[:] = 0
splits = pd.concat([new_splits, splits])
splits = splits.dropna(how='all')

splits = splits.drop(columns=["placeholder2"])
splits = splits.reindex(sorted(splits.columns), axis=1)


def update_early_cells_splits(column):
    first_non_na = column.first_valid_index()
    if first_non_na is not None:
        splits.loc[:first_non_na, column.name] = column[first_non_na]


splits.apply(update_early_cells_splits, axis=0)

splits = splits.fillna(method='ffill')

splits.to_csv('Stocks_Splits_10yr.csv')
