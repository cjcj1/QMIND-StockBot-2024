from urllib.request import urlopen, Request
import re
import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests, json, lxml
import numpy as np
import pandas as pd
from newspaper import Article
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class live_nlp:
    def __init__(self):
        pass

    def run_nlp(self, stock):
        #google search
        currentStock = stock + "+stock"
        BaseURL = "https://www.google.com/search?sca_esv=bcd8cd53e04dedb1&sxsrf=ACQVn08KSC8h2lXMkLo1lTlwMgmkJh1wpQ:1709011552016&q=TheStockSymbole&tbm=nws&source=lnms&prmd=znivsmbt&sa=X&sqi=2&pjf=1&ved=2ahUKEwingOaT5MqEAxXNrokEHWzLBuoQ0pQJegQIDBAB&biw=1440&bih=754&dpr=2"
        FinalURL = BaseURL.replace("TheStockSymbole", str(currentStock))

        req = Request(FinalURL, headers= {'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()

        reqs = requests.get(FinalURL)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        
        ArticleURLs = []
        CellsToDelete = []
        for link in soup.find_all('a'):
            ArticleURLs.append(link.get('href'))

        finalURLs1 = []
        finalURLs2 = []

        for i in range(len(ArticleURLs)):
            try:
                finalURLs1.append(ArticleURLs[i].split("?q=")[1])
            except Exception as e:
                CellsToDelete.append(i)
            #    del ArticleURLs[i]
            
        for i in range(len(finalURLs1)):
            try:
                finalURLs2.append(finalURLs1[i].split("&sa")[0])
            except Exception as e:
                CellsToDelete.append(i)
            #print(finalURLs2[i])
            #print('\n')
            a=1

        #Plug URLs into newspaper3k
        text_list = []

        for url in finalURLs2:
            if url.find("google.com") != -1:
                print(url)
                continue
            try:
                article = Article(url)
                article.download()
                article.parse()
                text_list.append(article.text.replace('\\n', ' ').replace("\n", ' '))
            except Exception as e:
                #print(f"Error processing URL {url}")
                a=1


        #plug article into NLP
        nltk.download('vader_lexicon')
        sia = SentimentIntensityAnalyzer()
        nlp_score = []

        for text in text_list:
            nlp_score.append(sia.polarity_scores(text)['compound'])
            

        print(nlp_score)
        return sum(nlp_score)/len(nlp_score)

