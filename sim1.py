import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')

def get_similarity(word1, word2):
    syns1 = wordnet.synsets(word1)
    syns2 = wordnet.synsets(word2)
    if not syns1 or not syns2:
        return 0
    sim_score = syns1[0].wup_similarity(syns2[0])
    return sim_score

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
similarity = get_similarity(word1, word2)
print(f"Similarity between {word1} and {word2} is {similarity}")
