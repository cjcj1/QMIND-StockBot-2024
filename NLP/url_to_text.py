import pandas as pd
from newspaper import Article

urls = pd.read_csv('URLs.csv', index_col=0)
text = urls.copy()

for month, row in urls.iterrows():
    for stock in urls.columns:
        urls_list = row[stock].split()
        text_list = []
        for url in urls_list:
            try:
                article = Article(url)
                article.download()
                article.parse()
                text_list.append(article.text.replace('\\n', ' ').replace("\n", ' '))
            except Exception as e:
                print(f"Error processing URL {url}")
        text.at[month, stock] = text_list

text.to_csv('NLP_TrainingData.csv')
