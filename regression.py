import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

adj = pd.read_csv('Stocks_AdjClose_3yr.csv', index_col=0, parse_dates=True)
vol = pd.read_csv('Stocks_Volume_3yr.csv', index_col=0, parse_dates=True)

adj.reset_index(inplace=True)

# Convert datetime to numerical values
adj['numeric_date'] = (adj['index'] - adj['index'].min()) / np.timedelta64(1, 'D')

stock = "AAPL"

x = adj['numeric_date'].values.reshape(-1, 1)
y = adj[stock]

lr_model = LinearRegression()
lr_model.fit(x, y)
y_pred = lr_model.predict(x)

plt.scatter(x, y)
plt.plot(x, y_pred)

plt.xlabel("Days since " + str(adj["index"].min().strftime("%Y-%m-%d")))
plt.ylabel("Price in USD")
plt.title(stock + " stock")

plt.show()