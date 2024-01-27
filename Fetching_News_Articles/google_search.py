from urllib.request import urlopen, Request
import re
import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests, json, lxml
import numpy as np


list_of_companies = pd.read_csv("/Users/marcoschapira/Documents/Qmind/QMIND-StockBot-2024/Fetching_News_Articles/S&P_500_Companies_list.csv")


def fetchCNBC ():
    #fetch html from website url
    url = Request('https://www.google.com/search?q=mmm+stock+news&sca_esv=583820872&biw=1440&bih=754&sxsrf=AM9HkKkNTXjbP_ikjdhjJAlxFmwyrv0HXA%3A1700422230486&source=lnt&tbs=cdr%3A1%2Ccd_min%3A10%2F1%2F2023%2Ccd_max%3A10%2F31%2F2023&tbm=nws',
                    headers={'User-Agent': 'Mozilla/5.0'})

    html_bytes = urlopen(url).read()

    #Convert html from byte type to string type
    html_string = html_bytes.decode("utf-8")

    return(html_string)


#articleDataSet[X][Y][Z]
NumberOfStocks = len(list_of_companies['Symbol']) #X Dimention
NumberOfMonths = 5 #Y Dimention
NumberOfSources = 2 #Z Dimention
articlesDataSet = [[ ['#' for col in range(NumberOfSources)] for col in range(NumberOfMonths)] for row in range(NumberOfStocks)]


for i in range(len(list_of_companies['Symbol'])) :
    articlesDataSet[i][0][0] = list_of_companies["Symbol"][i]

#Start loop to go through stocks
for stock in range(len(articlesDataSet)) :
    currentStock = articlesDataSet[stock][0][0]

    #google search
    BaseURL = "https://www.google.com/search?q=TheStockSymbole+stock&sca_esv=593898376&biw=1440&bih=754&sxsrf=AM9HkKnp3EVAK9TTE0qWa7LwoGfE51xdvA%3A1703652774577&source=lnt&tbs=cdr%3A1%2Ccd_min%3AStartMonth%2F1%2FSearchYEAR%2Ccd_max%3AEndMonth%2F1%2FSearchYEAR&tbm=nws"
    URLSymbole = BaseURL.replace("TheStockSymbole", str(currentStock))

    #Loop through years
    for year in range(2022, 2023):

        URLYear = URLSymbole.replace("SearchYEAR", str(year))

        #Loop through months
        for StartMonth in range(1, 11):
            Endmonth = StartMonth + 1
            URLMonth1 = URLYear.replace("StartMonth", str(StartMonth))
            FinalURL = URLMonth1.replace("EndMonth", str(Endmonth))

            #Look Up google page
            sources = ''

            req = Request(FinalURL, headers= {'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            with requests.Session() as c:
                soup = BeautifulSoup(webpage, 'html5lib')
                #print(soup)
                for link in soup.find_all('a', href=True):
                    sources = sources + link['href']

            

            break
        break
    break

            #articlesDataSet.loc[:,2]
    
    #for date in range(100): #change month

        #find articles for each source
    #    articlePlaceHolder = "abcd"

        #add articles to dataframe
    #    articlesDataSet.append(articlePlaceHolder)






