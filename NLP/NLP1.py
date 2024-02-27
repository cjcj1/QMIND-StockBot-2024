# Natural language toolkit is the library @ https://www.nltk.org/
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon for sentiment analysis, only have to run this line once, can comment
# out after

nltk.download('vader_lexicon')

# The article to analyze, try putting different words like positive, great etc. and watch the score
article = "terrible"


# NLP algorithm
def analyze_sentiment(text):
    # Using the prebuilt tool from the library
    sia = SentimentIntensityAnalyzer()

    """" The line below extracts the compound result from the nlp algorithm.
    The library returns 4 sentiment scores: positive, negative, neutral and compound.
    The Compound score is a normalized and weighted score that ranges from -1 to 1 with 1 being most positive """

    nlp_score = sia.polarity_scores(text)['compound']
    return nlp_score


# Prints the thresholds for the meaning of the compound value
def classify_sentiment(score):
    if score >= 0.05:
        return "Very Positive"
    elif 0.01 <= score < 0.05:
        return "Positive"
    elif -0.01 <= score <= 0.01:
        return "Neutral"
    elif -0.05 < score < -0.01:
        return "Negative"
    else:
        return "Very Negative"


# Analyze and classify sentiment
sentiment_score = analyze_sentiment(article)
sentiment_label = classify_sentiment(sentiment_score)

# Print the results
print(f"Sentiment Score: {sentiment_score}")
print(f"Sentiment Feeling: {sentiment_label}")