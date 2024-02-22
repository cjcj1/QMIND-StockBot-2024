import pandas as pd

urls = pd.read_csv('URLs.csv', index_col=0)
text = urls

print(urls.to_string())

for month, row in urls.iterrows():
    for stock in row:
        newCell = stock.split()
        cellIndex = 0
        for item in newCell:
            newItem = # web scraping for item
            newCell[cellIndex] = newItem
            cellIndex += 1
        text[month][stock] = newCell
