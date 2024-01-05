import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


# Create a SentimentIntensityAnalyzer object
analyzer = SentimentIntensityAnalyzer()

# Sample reviews (replace with your actual reviews)
reviews = [
    "This product was amazing! It exceeded my expectations and was easy to use.",
    "I was disappointed with the quality of this product. It felt cheap and broke easily.",
    "The customer service was excellent. They were very helpful and resolved my issue quickly.",
    "The shipping was delayed, and I didn't receive the product on time.",
]

# Analyze the sentiment of each review and assign star ratings
for review in reviews:
    scores = analyzer.polarity_scores(review)
    compound_score = scores['compound']

    # Map compound score to star rating (adjust thresholds as needed)
    if compound_score >= 0.4:
        stars = 5
    elif compound_score >= 0.2:
        stars = 4
    elif compound_score >= 0:
        stars = 3
    elif compound_score >= -0.2:
        stars = 2
    else:
        stars = 1

    print(f"Review: {review}")
    print(f"Sentiment: {scores}")
    print(f"Star Rating: {stars}\n")