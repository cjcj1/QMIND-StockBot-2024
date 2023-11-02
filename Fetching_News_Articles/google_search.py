import requests
from urllib.request import urlopen, Request

from selenium import webdriver
import time

url = Request('https://www.google.com/search?q=tesla+stock+new&sca_esv=565418613&biw=1440&bih=758&sxsrf=AM9HkKkdaWRGxmJEKkJIg3043I7E-M2NOA%3A1694735344218&source=lnt&tbs=cdr%3A1%2Ccd_min%3A9%2F1%2F2022%2Ccd_max%3A10%2F1%2F2022&tbm=nws',
                headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(url).read()
html = response.read().decode("utf-8")

print("asadsd;flkajsd;flaksdjf;aslkdj")