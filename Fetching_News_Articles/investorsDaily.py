# Import libraries
from urllib.request import urlopen, Request
import re

# Fetch HTML from website URL
url = Request('https://www.investors.com/research/apple-stock-buy-now/',
              headers={'User-Agent': 'Mozilla/5.0'})
html_bytes = urlopen(url).read()

# Convert HTML from byte type to string type
html_string = html_bytes.decode("utf-8")

###########################################
#### Specific to each news source due to HTML structure differences
###########################################

# Find the index of the class name for the div tag where the article starts
starting_flag = "class=\"single-post-content post-content drop-cap crawler\""
start_index = html_string.find(starting_flag)

# Set start after the div tag
start_content_index = html_string.find('>', start_index) + 1

# Find the index of the phrase that indicates the end of the article
end_flag = '<strong>YOU MAY ALSO LIKE:</strong>'
end_index = html_string.find(end_flag)

# Check that both the start and end indices were found
if start_content_index != -1 and end_index != -1:
    # Extract the article using the indices to get the substring
    article = html_string[start_content_index:end_index]
    
    # Remove JSON-LD script from the article
    article_without_json_ld = re.sub(r'<script type="application/ld\+json">.*?</script>', '', article, flags=re.DOTALL)

    # Clean the article to remove HTML tags and script tags
    clean_article = re.sub(r'<[^>]*>', '', article_without_json_ld)

    # Add a newline after periods that are likely the end of sentences
    enhanced_article = re.sub(r'\.\s([A-Z])', r'.\n\n\1', clean_article)
    
    # Remove lines that only contain 'X' with optional whitespace
    final_article = re.sub(r'^\s*X\s*$', '', enhanced_article, flags=re.MULTILINE)
    # This was neccesary to remove some weird glitch from appearing
    
    # Print the final article
    print(final_article)
else:
    # If start or end indices are not found, handle this case
    print("Could not find the start or end of the article content.")
