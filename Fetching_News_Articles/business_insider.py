#import libraries
from urllib.request import urlopen, Request
import re

#fetch html from website url
url = Request('https://www.businessinsider.com/exxon-mobil-rex-tillerson-made-274-million-as-ceo-last-year-2017-4',
                headers={'User-Agent': 'Mozilla/5.0'})


html_bytes = urlopen(url).read()

#Convert html from byte type to string type
html_string = html_bytes.decode("utf-8")

###########################################
#### !!! Below is the part that cheanged for every news source because the flags need to be different
###########################################

#establish around where news articles start and end (start slightly befoe and end slightly after)
starting_flag = html_string.find("class=\"content-lock-content\"")
end_flag = html_string.find("class=\"post-content-more\"")

#Save trimmed article as a string
article = html_string[starting_flag + 130:end_flag]


firstbracketopen = article.find("<")
firstbracketclose = article.find(">")

if (firstbracketclose < firstbracketopen):
	parttoremovefirst = article[1:firstbracketclose+1]
	article = article.replace(parttoremovefirst, '')

#print(article)

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

    #Code to remove selected part to remove
    article = article.replace(part_to_remove, '')

#print final article
print(article)