# Requires pre-trained GoogleNews Word2Vec model for this example

import nltk
from nltk.corpus import wordnet as wn
#from gensim.models import KeyedVectors
from nltk.tokenize import word_tokenize
import numpy as np

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

print("Loading Word2Vec Model, this might take a moment")
w2v = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

def vectorize_text(text):
    tokens = [t.lower() for t in word_tokenize(text) if t.isalpha()]
    vectors = [w2v[t] for t in tokens if t in w2v]
    return np.mean(vectors, axis=0) if vectors else np.zeros(w2v.vector_size)

def wsd_word2vec(sentence, target_word):
    senses = wn.synsets(target_word)
    if not senses:
        return None
    tokens = word_tokenize(sentence)
    context = " ".join([t for t in tokens if t.lower() != target_word.lower()])
    context_vec = vectorize_text(context)
    scored_senses = []
    for syn in senses:
        gloss = syn.definition() + " " + " ".join(syn.examples())
        gloss_vec = vectorize_text(gloss)
        if np.linalg.norm(gloss_vec) > 0:
            similarity = np.dot(context_vec, gloss_vec) / (np.linalg.norm(context_vec) * np.linalg.norm(gloss_vec))
        else:
            similarity = 0
        scored_senses.append((syn, similarity))
    return max(scored_senses, key=lambda x: x[1]), scored_senses

sentence = "I went to the bank to withdraw money"
target = "bank"
best, all_scores = wsd_word2vec(sentence, target)
if best:
    print(f"Best Sense: {best[0].name()} - {best[0].definition()}")
    for syn, score in all_scores[:5]:
        print(f"{syn.name():20} score = {score:.4f} - {syn.definition()}")
else:
    print("No sense found")
