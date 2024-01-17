# Import libraries
from urllib.request import urlopen, Request
import re

# Fetch HTML from website URL
url = Request('https://www.fool.com/investing/2024/01/04/apples-85-billion-services-business-is-less-profit/',
              headers={'User-Agent': 'Mozilla/5.0'})
html_bytes = urlopen(url).read()

# Convert HTML from byte type to string type
html_string = html_bytes.decode("utf-8")

###########################################
#### Specific to each news source due to HTML structure differences
###########################################

# Find the index of the class name for the div tag where the article starts
starting_flag = "class=\"article-body\""
start_index = html_string.find(starting_flag)
print("Start index:", start_index) 

# Set start after the div tag
start_content_index = html_string.find('>', start_index) + 1
print("Start content index:", start_content_index) 

# Find the index of the phrase that indicates the end of the article
end_flag = 'class="article-pitch-container"'
end_index = html_string.find(end_flag)
print("End index:", end_index) 

if start_content_index != -1 and end_index != -1:
    # Extract the article using the indices to get the substring
    article = html_string[start_content_index:end_index]

    # Remove script tags and their content
    article = re.sub(r'<script[^<]*</script>', '', article, flags=re.DOTALL)
    
    # Remove remaining HTML tags to isolate text
    clean_article = re.sub(r'<[^>]+>', '', article, flags=re.DOTALL)
    
    # Print the cleaned article
    print(clean_article)
else:
    # If start or end indices are not found, handle this case
    print("Could not find the start or end of the article content.")