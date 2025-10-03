import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('wordnet')

s1 = "he sat on the bank of the river"
s2 = "she went to the bank to deposit money"

t1 = word_tokenize(s1)
t2 = word_tokenize(s2)

sense1 = lesk(t1, 'bank')
sense2 = lesk(t2, 'bank')

print("context 1:", s1)
print("sense:", sense1)
print("definition:", sense1.definition())

print("\ncontext 2:", s2)
print("sense:", sense2)
print("definition:", sense2.definition())
