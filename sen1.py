import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    compound = scores['compound']
    
    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return scores, sentiment

def main():
    print("Sentiment Analysis using NLTK VADER")
    while True:
        text = input("Enter a sentence: ").strip()
        if text.lower() == "exit":
            print("\nThanks for using Sentiment Analysis!")
            break
        
        scores, sentiment = analyze_sentiment(text)
        print("\nSentiment Scores:", scores)
        print("Overall Sentiment:", sentiment)
        print("-" * 50)

if __name__ == "__main__":
    main()