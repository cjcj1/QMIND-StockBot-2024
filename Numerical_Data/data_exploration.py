import pandas as pd
import matplotlib.pyplot as plt

# reading data from csv
adj = pd.read_csv('Stocks_AdjClose_10yr.csv', index_col=0, parse_dates=True)
vol = pd.read_csv('Stocks_Volume_10yr.csv', index_col=0, parse_dates=True)
div = pd.read_csv('Stocks_Dividends_10yr.csv', index_col=0, parse_dates=True)
spl = pd.read_csv('Stocks_Splits_10yr.csv', index_col=0, parse_dates=True)

# plotting data
plt.scatter(adj.index, adj["AAPL"], label='Data Points')
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Adjusted Close')
plt.title('AAPL')
plt.subplots_adjust(bottom=0.2)
plt.show()
