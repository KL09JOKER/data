import spacy

nlp = spacy.load("en_core_web_sm")
sentence = "Natural language Processing is an exciting field of AI."
doc = nlp(sentence)

print("POS Tags:")
for token in doc:
    print(f"{token.text} → {token.pos_} ({token.tag_})")
