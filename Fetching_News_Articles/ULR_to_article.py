import pandas as pd

from NewsSources import NewsSources

urlTable = pd.read_csv("/Users/marcoschapira/Documents/Qmind/QMIND-StockBot-2024/Fetching_News_Articles/Website_URLs.csv")

News = NewsSources()

for date in range(4):

    print(urlTable.iat[date,0])

    for stock in range(18):
        print(urlTable.iat[date,stock])
        cell = urlTable.iat[date,stock]
        splitUpCell = cell.split()
        for i in range(len(splitUpCell)):
            CurrentURL = splitUpCell[i]
            #switch case
            #call function from news sources class

CurrentURL = "https://www.cnbc.com/2023/11/09/tesla-stock-drops-5percent-after-hsbc-calls-it-a-very-expensive-auto-company.html"
#abc = News.cnbc(CurrentURL)

