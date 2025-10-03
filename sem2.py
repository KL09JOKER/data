import spacy
from keybert import KeyBERT

nlp = spacy.load('en_core_web_md')
kw_model = KeyBERT()

def analyze_similarity(sent1, sent2):
    doc1, doc2 = nlp(sent1), nlp(sent2)
    return doc1.similarity(doc2)

def extract_keywords(text, n=5):
    return kw_model.extract_keywords(text, top_n=n)

def main():
    print("Semantic Analyzer in NLP")
    sent1 = "The quick brown fox jumps over the lazy dog."
    sent2 = "A fast brown fox leaps over a sleepy dog."
    
    sim = analyze_similarity(sent1, sent2)
    print(f"\nSemantic similarity between sentences: {sim:.2f}\n")
    
    text = "Natural language processing enables computers to understand human language. Applications include translation, sentiment analysis, and chatbots."
    keywords = extract_keywords(text)
    
    print("\nTop Keywords:")
    for kw, score in keywords:
        print(f"- {kw} (score: {score:.2f})")
    
    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()
