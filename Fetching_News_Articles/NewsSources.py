from urllib.request import urlopen, Request
import re

class NewsSources:

    def __init__(self) -> None:
        pass

    def cnbc(self, theURL):

        #fetch html from website url
        url = Request(theURL,
                        headers={'User-Agent': 'Mozilla/5.0'})

        #https://www.cnbc.com/2023/10/30/tesla-shares-drop-5percent-on-panasonic-battery-warning.html
        #https://www.cnbc.com/2023/11/02/apple-aapl-earnings-report-q4-2023.html

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
        return article

    def themotlyfool(self, theURL):
        # Fetch HTML from website URL
        url = Request(theURL,
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

    def investorsDaily(self, theURL):
        # Fetch HTML from website URL
        url = Request(theURL,
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

