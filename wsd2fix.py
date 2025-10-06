import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
nltk.download("wordnet")
nltk.download("omw-1.4")
s1="i went bank to deposit"
s2="i went to river bank"
sence1=lesk(s1.split(),"bank")
sence2=lesk(s2.split(),"bank")
print("sentance ",s1)
print("sense ",sence1)
print("definition ",sence1.definition())
print("sentance ",s2)
print("sense ",sence2)
print("definition ",sence2.definition())