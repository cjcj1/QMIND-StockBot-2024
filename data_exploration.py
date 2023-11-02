import pandas as pd
from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()

tickers = ["AAPL", "AMZN", "GOOG"]

df = yf.download(tickers, start="2023-09-01", end="2023-09-30")
print(df.to_string())
print("hi")
