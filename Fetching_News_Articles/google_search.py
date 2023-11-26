from urllib.request import urlopen, Request
import re
import csv
import pandas as pd

list_of_companies = pd.read_csv("/Users/marcoschapira/Documents/Qmind/QMIND-StockBot-2024/Fetching_News_Articles/S&P_500_Companies_list.csv")


#fetch html from website url
url = Request('https://www.google.com/search?q=mmm+stock+news&sca_esv=583820872&biw=1440&bih=754&sxsrf=AM9HkKkNTXjbP_ikjdhjJAlxFmwyrv0HXA%3A1700422230486&source=lnt&tbs=cdr%3A1%2Ccd_min%3A10%2F1%2F2023%2Ccd_max%3A10%2F31%2F2023&tbm=nws',
                headers={'User-Agent': 'Mozilla/5.0'})

html_bytes = urlopen(url).read()

#Convert html from byte type to string type
html_string = html_bytes.decode("utf-8")


