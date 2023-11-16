from selenium import webdriver
import time

#open firefox
browser=webdriver.Firefox()
browser.get("https://finance.yahoo.com/news/stock-market-news-live-updates-september-29-2022-105414183.html")

#wait 10 second to let firefox open and page to fully load
time.sleep(10)

#save html into string
html = browser.page_source

#close web browser
browser.close()

#print html from page
#print(html)

place = html.find("if(!window.finWebCore){window.finWebCore=function r(e){const{isModern:t=!0,isDev:i=!1,lang:o=s,devAssets:a,prodAssets:r,crumb:n=")


print(len(html))
print(html[place:place+100])