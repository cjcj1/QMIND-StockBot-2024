import numpy as np
import pandas as pd


list_of_companies = pd.read_csv("/Users/marcoschapira/Documents/Qmind/QMIND-StockBot-2024/Fetching_News_Articles/S&P_500_Companies_list.csv")

NumberOfStocks = len(list_of_companies['Symbol']) #X Dimention
NumberOfMonths = 2 #Y Dimention
NumberOfSources = 2 #Z Dimention

#articleDataSet[X][Y][Z]
articlesDataSet = [[ ['#' for col in range(NumberOfSources)] for col in range(NumberOfMonths)] for row in range(NumberOfStocks)]

for i in range(len(list_of_companies['Symbol'])) :
    articlesDataSet[i][0][0] = list_of_companies["Symbol"][i]


print(articlesDataSet[:][:][:])