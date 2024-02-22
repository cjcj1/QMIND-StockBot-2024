import pandas as pd

urls = pd.read_csv('URLs.csv', index_col=0)

print(urls.to_string())

for month, row in urls.iterrows():
    for stock in row:
        newCell = stock.split()
        for link in newCell:
            # set link equal to text version of link using web scraping