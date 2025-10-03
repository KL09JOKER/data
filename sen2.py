from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return polarity, subjectivity, sentiment

def main():
    print("Sentiment Analysis using TextBlob")
    while True:
        text = input("Enter a sentence: ").strip()
        if text.lower() == "exit":
            print("\nGoodbye!")
            break
        
        polarity, subjectivity, sentiment = analyze_sentiment(text)
        
        print(f"\nPolarity: {polarity:.3f}")
        print(f"Subjectivity: {subjectivity:.3f}")
        print("Overall Sentiment:", sentiment)
        print("-" * 50)

if __name__ == "__main__":
    main()
