from urllib.request import urlopen, Request
import re
from bs4 import BeautifulSoup



#fetch html from website url
url = Request('https://duckduckgo.com/?q=Tesla+stock+news&t=h_&df=2021-01-01..2021-01-29&ia=web',
                headers={'User-Agent': 'Mozilla/5.0'})

html_bytes = urlopen(url).read()

#Convert html from byte type to string type
html_string = html_bytes.decode("utf-8")

print(html_string)

soup = BeautifulSoup( html_string , 'html.parser') 
  
# Finding by class name 
#print(soup.find( class_ = "tHmfQe" ))
print(html_string)
