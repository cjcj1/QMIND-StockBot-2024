import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# reading data from csv
adj = pd.read_csv('Stocks_AdjClose_3yr.csv')
vol = pd.read_csv('Stocks_Volume_3yr.csv')

# changing index to datetime
timestamps = pd.to_datetime(adj.index).astype('int64').astype(int) / 10**9

# calculating linear regression
lin_reg = LinearRegression().fit(timestamps.values.reshape(-1, 1), adj["AAPL"])
coefficients = np.polyfit(timestamps, adj["AAPL"], 1)

# plotting linear regression
plt.scatter(adj.index, adj["AAPL"], label='Data Points')
plt.plot(adj.index, coefficients[0] * timestamps + coefficients[1], color='red', label='Linear Regression')
plt.xlabel('')
plt.xticks([])
plt.ylabel('Adjusted Close')
plt.legend().set_visible(False)
plt.title('AAPL')
plt.show()
