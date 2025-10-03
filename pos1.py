import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "She is reading NLP book."
words = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(words)

print("Parts of Speech:")
for word, tag in pos_tags:
    print(f"{word:10} → {tag}")
