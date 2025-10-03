import spacy

nlp = spacy.load("en_core_web_md")

w1 = nlp("king")
w2 = nlp("queen")
w3 = nlp("apple")

print(f"king~queen: {w1.similarity(w2):.4f}")
print(f"king~apple: {w1.similarity(w3):.4f}")

words = ["king", "queen", "prince", "car", "apple"]
for a in words:
    for b in words:
        if a != b:
            print(f"{a}->{b}: {nlp(a).similarity(nlp(b)):.4f}")
