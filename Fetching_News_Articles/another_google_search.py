from selenium import webdriver
import time
from bs4 import BeautifulSoup

import smtplib

browser=webdriver.Firefox()

# get source code
browser.get("https://www.google.com/search?q=tesla+stock&sca_esv=593898376&biw=1440&bih=754&sxsrf=AM9HkKn9AmRmyfq85JhegaK-DGLuv1hwyg%3A1704664098517&source=lnt&tbs=cdr%3A1%2Ccd_min%3A11%2F1%2F2023%2Ccd_max%3A11%2F30%2F2023&tbm=nws")

time.sleep(10)
html = browser.page_source
#print(html)
# close web browser
browser.close()

soup = BeautifulSoup( html , 'html.parser') 
  
# Finding by class name 
print(soup.find( class_ = "tHmfQe" ))

