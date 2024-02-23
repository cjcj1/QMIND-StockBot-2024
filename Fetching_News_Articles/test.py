import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


file_path = '/Users/marcoschapira/Documents/Qmind/QMIND-StockBot-2024/DataSets/'  
df = pd.read_csv(file_path + 'Stocks_AdjClose_10yr.csv')#, index_col=1, parse_dates=True)
StockDividends = pd.read_csv(file_path + 'Stocks_Dividends_10yr.csv')#, index_col=1, parse_dates=True)
StocksSplits = pd.read_csv(file_path + 'Stocks_Splits_10yr.csv')#, index_col=1, parse_dates=True)
StocksVolume = pd.read_csv(file_path + 'Stocks_Volume_10yr.csv')#, index_col=1, parse_dates=True)

df = df.drop('Unnamed: 0', axis=1)
StockDividends = StockDividends.drop('Unnamed: 0', axis=1)
StocksSplits = StocksSplits.drop('Unnamed: 0', axis=1)
StocksVolume = StocksVolume.drop('Unnamed: 0', axis=1)

scaler = MinMaxScaler()

#print(df.loc[0, :])

# Initialize the Min-Max Scaler
scaler = MinMaxScaler()

# Scale the dataset
scaled_PriceData = scaler.fit_transform(df.values)
scaled_DividendsData = scaler.fit_transform(StockDividends.values)
scaled_SplitsData = scaler.fit_transform(StocksSplits.values)
scaled_VolumeData = scaler.fit_transform(StocksVolume.values)

#print(scaled_PriceData)


################################
#Need to make new def below that splits up datasets into different datasets for each stock
################################

NumberOfStocks = scaled_PriceData.shape[1] #X Dimention
NumberOfDays = scaled_PriceData.shape[0] #Y Dimention
NumberOfdatasets = 4 #Z Dimention
TheDataset = [[ ['#' for col in range(NumberOfdatasets)] for col in range(NumberOfDays)] for row in range(NumberOfStocks)]

NumberOfRows = NumberOfDays
tempDataSet = pd.DataFrame(index=np.arange(NumberOfRows), columns=['Price', 'Volume']) #, 'Dividends'])

#print(scaled_PriceData.shape[0])
print(scaled_SplitsData[114][114])

SaveingLocation = '/Users/marcoschapira/Documents/Qmind/QMIND-StockBot-2024/DataSets/ByStock/'

for Stock in range(scaled_PriceData.shape[1]):
  for day in range(scaled_PriceData.shape[0]):       
    tempDataSet.loc[day][0] = scaled_PriceData[day][Stock]
    tempDataSet.loc[day][1] = scaled_VolumeData[day][Stock]
    #tempDataSet.loc[day][2] = scaled_DividendsData[day][Stock]
    #tempDataSet.loc[day][3] = scaled_SplitsData[day][Stock]

    print(scaled_PriceData[day][Stock])

  tempDataSet.to_csv(SaveingLocation + 'Stock' + str(Stock) + '.csv', index=False)



'''

def create_sequences(data, sequence_length):
    xs = []
    ys = []
    for i in range(len(data)-sequence_length):
        x_part = data[i:i+sequence_length]
        y_part = data[i+sequence_length]
        xs.append(x_part)
        ys.append(y_part)
    return np.array(xs), np.array(ys)

# Choose a sequence length
sequence_length = 60  # Number of days to use for prediction. Adjust as needed.

# Create the sequences
X, y = create_sequences(scaled_PriceData, sequence_length)

train_size = int(len(X) * 0.8)  # 80% for training, 20% for testing
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

'''