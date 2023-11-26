import pandas
import pandas as pd
from pandas_datareader import data as pdr
from datetime import date
from datetime import datetime
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

yf.pdr_override()

tickers = ["AAPL"]
startDate = "2023-2-01"
endDate = "2023-11-16"


df = yf.download(tickers, start=startDate, end=endDate)
df.reset_index(inplace=True)

df['Date'] = df['Date'].dt.strftime('%b %d')

sns.lineplot(x='Date', y='Open', data=df)


# Make the X axis neater by lowering number of labels and tilting them

# Convert the date strings to datetime objects
start_date = datetime.strptime(startDate, "%Y-%m-%d")
end_date = datetime.strptime(endDate, "%Y-%m-%d")

# Calculate the day range
day_range = (end_date - start_date).days

# Rotate the labels
plt.xticks(rotation=45)

# Set the X axis labels to be dependent on the day range
interval = int(day_range/10)
tick_indices = df.index[::interval]
tick_labels = df['Date'].iloc[::interval]
plt.xticks(tick_indices, tick_labels)

plt.title(f"{tickers[0]} Stock from {startDate} to {endDate}")
plt.show()

