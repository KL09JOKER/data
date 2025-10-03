import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

text = "NLP is a field of AI. It deals with analyzing human language!"

print("Sentence Tokenization:")
print(sent_tokenize(text))

print("\nWord Tokenization:")
words = word_tokenize(text)
print(words)

print("\nStopword Removal:")
stop_words = set(stopwords.words('english'))
filtered_words = [w for w in words if w.lower() not in stop_words]
print(filtered_words)

print("\nStemming:")
ps = PorterStemmer()
stemmed_words = [ps.stem(w) for w in filtered_words]
print(stemmed_words)

print("\nLemmatization:")
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(w.lower()) for w in filtered_words]
print(lemmatized_words)

print("\nFinal Lexical Form of sentence:")
print(" ".join(lemmatized_words))
