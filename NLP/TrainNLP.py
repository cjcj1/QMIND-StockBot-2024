import pandas as pd
import numpy as np
from textblob import TextBlob

df = pd.read_csv('NLP_TrainingData.csv', index_col=0)
df = df.dropna()
adj = pd.read_csv('Stocks_AdjClose_10yr.csv', index_col=0, parse_dates=True)

print(df.head())

correct = 0
total = 0

# Apr-17
for col in df.columns:
    test = adj[col].loc["2017-05-01":"2017-05-31"]
    slope, intercept = np.polyfit(range(len(test)), test, 1)
    if (isinstance(df[col]['Apr-17'], str)):
        nlp_score = TextBlob(df[col]['Apr-17']).sentiment.polarity
        if nlp_score > 0 and slope > 0:
            correct += 1
        elif nlp_score <= 0 and slope <= 0:
            correct += 1
        total += 1
    else:
        for text in df[col]['Apr-17']:
            nlp_score = TextBlob(text).sentiment.polarity
            if nlp_score > 0 and slope > 0:
                correct += 1
            elif nlp_score <= 0 and slope <= 0:
                correct += 1
            total += 1

# Jul-19
for col in df.columns:
    test = adj[col].loc["2019-08-01":"2019-08-31"]
    slope, intercept = np.polyfit(range(len(test)), test, 1)
    if (isinstance(df[col]['Jul-19'], str)):
        nlp_score = TextBlob(df[col]['Jul-19']).sentiment.polarity
        if nlp_score > 0 and slope > 0:
            correct += 1
        elif nlp_score <= 0 and slope <= 0:
            correct += 1
        total += 1
    else:
        for text in df[col]['Jul-19']:
            nlp_score = TextBlob(text).sentiment.polarity
            if nlp_score > 0 and slope > 0:
                correct += 1
            elif nlp_score <= 0 and slope <= 0:
                correct += 1
            total += 1

# Oct-20
for col in df.columns:
    test = adj[col].loc["2020-11-01":"2020-11-30"]
    slope, intercept = np.polyfit(range(len(test)), test, 1)
    if (isinstance(df[col]['Oct-20'], str)):
        nlp_score = TextBlob(df[col]['Oct-20']).sentiment.polarity
        if nlp_score > 0 and slope > 0:
            correct += 1
        elif nlp_score <= 0 and slope <= 0:
            correct += 1
        total += 1
    else:
        for text in df[col]['Oct-20']:
            nlp_score = TextBlob(text).sentiment.polarity
            if nlp_score > 0 and slope > 0:
                correct += 1
            elif nlp_score <= 0 and slope <= 0:
                correct += 1
            total += 1

# Jul-21
for col in df.columns:
    test = adj[col].loc["2021-08-01":"2021-08-31"]
    slope, intercept = np.polyfit(range(len(test)), test, 1)
    if (isinstance(df[col]['Jul-21'], str)):
        nlp_score = TextBlob(df[col]['Jul-21']).sentiment.polarity
        if nlp_score > 0 and slope > 0:
            correct += 1
        elif nlp_score <= 0 and slope <= 0:
            correct += 1
        total += 1
    else:
        for text in df[col]['Jul-21']:
            nlp_score = TextBlob(text).sentiment.polarity
            if nlp_score > 0 and slope > 0:
                correct += 1
            elif nlp_score <= 0 and slope <= 0:
                correct += 1
            total += 1

print(str(correct) + " out of " + str(total))
print(str(int(correct / total * 100)) + "% Accuracy")
