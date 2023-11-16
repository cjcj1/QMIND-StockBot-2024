#import libraries
from urllib.request import urlopen, Request
import re

#fetch html from website url
url = Request('https://www.cnbc.com/2023/11/02/apple-aapl-earnings-report-q4-2023.html',
                headers={'User-Agent': 'Mozilla/5.0'})

html_bytes = urlopen(url).read()

#Convert html from byte type to string type
html_string = html_bytes.decode("utf-8")

###########################################
#### !!! Below is the part that cheanged for every news source because the flags need to be different
###########################################

#establish around where news articles start and end (start slightly befoe and end slightly after)
starting_flag = html_string.find("class=\"ArticleBody-articleBody\"")
end_flag = html_string.find("class=\"SidebarArticle-sidebar PageBuilder-sidebar\"")

#Save trimmed article as a string
article = html_string[starting_flag + 130:end_flag]


##########################################
### !!! remove line below for other news sources
##########################################

#get rid of first ">"
article = article.replace('articleBody-6-2\">', '')


#initialize strings
new_part_to_remove = "b"
part_to_remove = "a"

#Loop to get rid of all code in between "<" and ">" brackets
while (article.find("<") != -1) & (article.find(">") != -1) & (part_to_remove != new_part_to_remove): 
    #find first "<" and ">" in string
    start = article.find("<")
    end = article.find(">")

    #code to make sure loop isn't stuck and previous part was removed
    new_part_to_remove = part_to_remove
    part_to_remove = article[start:end+1]
    print(part_to_remove + "\n\n\n\n")

    #Code to remove selected part to remove
    article = article.replace(part_to_remove, '')

#print final article
print(article)