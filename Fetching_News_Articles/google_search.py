from urllib.request import urlopen, Request
import re
import csv
import pandas as pd

import numpy


list_of_companies = pd.read_csv("/Users/marcoschapira/Documents/Qmind/QMIND-StockBot-2024/Fetching_News_Articles/S&P_500_Companies_list.csv")


def fetchCNBC ():
    #fetch html from website url
    url = Request('https://www.google.com/search?q=mmm+stock+news&sca_esv=583820872&biw=1440&bih=754&sxsrf=AM9HkKkNTXjbP_ikjdhjJAlxFmwyrv0HXA%3A1700422230486&source=lnt&tbs=cdr%3A1%2Ccd_min%3A10%2F1%2F2023%2Ccd_max%3A10%2F31%2F2023&tbm=nws',
                    headers={'User-Agent': 'Mozilla/5.0'})

    html_bytes = urlopen(url).read()

    #Convert html from byte type to string type
    html_string = html_bytes.decode("utf-8")

    return(html_string)
    
articlesDataSet = list_of_companies["Symbol"]

for stock in range(len(articlesDataSet)) : #change stock
    currentStock = articlesDataSet[stock+480]

    #google search
    BaseURL = "https://www.google.com/search?q=TheStockSymbole+stock&sca_esv=593898376&biw=1440&bih=754&sxsrf=AM9HkKnp3EVAK9TTE0qWa7LwoGfE51xdvA%3A1703652774577&source=lnt&tbs=cdr%3A1%2Ccd_min%3AStartMonth%2F1%2FSearchYEAR%2Ccd_max%3AEndMonth%2F1%2FSearchYEAR&tbm=nws"

    URLSymbole = BaseURL.replace("TheStockSymbole", str(currentStock))

    for year in range(2022, 2023):

        URLYear = URLSymbole.replace("SearchYEAR", str(year))

        for StartMonth in range(1, 11):
            Endmonth = StartMonth + 1
            URLMonth1 = URLYear.replace("StartMonth", str(StartMonth))
            FinalURL = URLMonth1.replace("EndMonth", str(Endmonth))

            #Look Up google page
            url = Request('https://www.google.com/search?q=WDC+stock&sca_esv=593898376&biw=1440&bih=754&sxsrf=AM9HkKnp3EVAK9TTE0qWa7LwoGfE51xdvA%3A1703652774577&source=lnt&tbs=cdr%3A1%2Ccd_min%3A1%2F1%2F2022%2Ccd_max%3A2%2F1%2F2022&tbm=nws',
                headers={'User-Agent': 'Mozilla/5.0'})
            googleHTML_bytes = urlopen(url).read()
            #Convert html from byte type to string type
            googleHTML_string = googleHTML_bytes.decode("utf-8")

            print(FinalURL)
            print(googleHTML_string)

            print(googleHTML_string.find("cnbc"))
            if(googleHTML_string.find("cnbc") != -1):
                print("yay")

            break
        break
    break

            #articlesDataSet.loc[:,2]
    
    #for date in range(100): #change month

        #find articles for each source
    #    articlePlaceHolder = "abcd"

        #add articles to dataframe
    #    articlesDataSet.append(articlePlaceHolder)






