from urllib.request import urlopen, Request
import re
import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests, json, lxml
import numpy as np


#fetch html from website url
url = Request('https://www.google.com/search?q=tesla+stock&sca_esv=593898376&biw=1440&bih=754&sxsrf=AM9HkKn9AmRmyfq85JhegaK-DGLuv1hwyg%3A1704664098517&source=lnt&tbs=cdr%3A1%2Ccd_min%3A11%2F1%2F2023%2Ccd_max%3A11%2F30%2F2023&tbm=nws',
                headers={'User-Agent': 'Mozilla/5.0'})

html_bytes = urlopen(url).read()

#Convert html from byte type to string type
html_string = html_bytes.decode("utf-8")

print(html_string)

soup = BeautifulSoup( html_string , 'html.parser') 
  
# Finding by class name 
print(soup.find( class_ = "tHmfQe" ))

