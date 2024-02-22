import pandas as pd
import matplotlib.pyplot as plt
from xgboost import XGBRegressor

df = pd.read_csv('Stocks_AdjClose_10yr.csv', index_col=0, parse_dates=True)

train = df.head(int(len(df)*0.8))
test = df.tail(int(len(df)*0.2))

X_train = train.index.to_series().apply(lambda x: x.toordinal()).values.reshape(-1, 1)
y_train = train['AAPL']
X_test = test.index.to_series().apply(lambda x: x.toordinal()).values.reshape(-1, 1)
y_test = test['AAPL']

xgb = XGBRegressor(n_estimators=100, max_depth=5)
xgb.fit(X_train, y_train)

y_pred = xgb.predict(X_test)

plt.plot(X_test, y_test, label='y_test')
plt.plot(X_test, y_pred, label='y_pred')
plt.ylabel('Price')
plt.legend()

plt.show()

