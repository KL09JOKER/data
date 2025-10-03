import spacy

nlp = spacy.load("en_core_web_sm")
text = "Barack Obama visited Paris in 2010."
doc = nlp(text)

print("\nNamed Entities:")
for ent in doc.ents:
    print(f"- {ent.text} ({ent.label_})")

print("\nPart-of-Speech Tagging:")
for token in doc:
    print(f"- {token.text}: {token.pos_}")

print("\nDependency Parsing:")
for token in doc:
    print(f"- {token.text:<12} {token.dep_:<10} --> {token.head.text}")

print("\nSimple Subject-Verb-Object Triplets:")
for token in doc:
    if token.dep_ == "ROOT":
        subject = [w for w in token.lefts if w.dep_ in ("nsubj", "nsubjpass")]
        obj = [w for w in token.rights if w.dep_ in ("dobj", "attr", "prep", "pobj")]
        
        if subject:
            print(f"Subject: {subject[0]}, Verb: {token}, Object: {obj[0] if obj else 'N/A'}")
