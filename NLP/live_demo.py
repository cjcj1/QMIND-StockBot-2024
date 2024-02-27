from urllib.request import urlopen, Request
import re
import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests, json, lxml
import numpy as np

#google search

currentStock = "tesla" + "+stock"
BaseURL = "https://www.google.com/search?sca_esv=bcd8cd53e04dedb1&sxsrf=ACQVn08KSC8h2lXMkLo1lTlwMgmkJh1wpQ:1709011552016&q=TheStockSymbole&tbm=nws&source=lnms&prmd=znivsmbt&sa=X&sqi=2&pjf=1&ved=2ahUKEwingOaT5MqEAxXNrokEHWzLBuoQ0pQJegQIDBAB&biw=1440&bih=754&dpr=2"
FinalURL = BaseURL.replace("TheStockSymbole", str(currentStock))

req = Request(FinalURL, headers= {'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

reqs = requests.get(FinalURL)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
ArticleURLs = []
CellsToDelete = []
for link in soup.find_all('a'):
    #print(link.get('href'))
    ArticleURLs.append(link.get('href'))

for i in range(len(ArticleURLs)):
    try:
        ArticleURLs[i] = ArticleURLs[i].split("?q=")[1]
    except Exception as e:
        CellsToDelete.append(i)
    ArticleURLs[i] = ArticleURLs[i].split("&sa")[0]

for i in range(len(CellsToDelete), 0, 1):
    ArticleURLs.pop(CellsToDelete[i])
    
for i in range(len(ArticleURLs)):
    print(ArticleURLs[i])


#write code to get rid of all google urls
#copy connor's code for getting artiles


#with requests.Session() as c:
    #soup = BeautifulSoup(webpage, 'html5lib')
    #print(soup)
    #for link in soup.find_all('a', href=True):
    #    sources = link['href']
    #    print(sources)
    #    break


