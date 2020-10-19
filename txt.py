from nltk import *
from nltk.text import Text
import urllib.request

def lexical_diversity(text) :
    return len(text) / len(set(text))

url = "http://www.gutenberg.org/files/28054/28054-0.txt"
raw = urllib.request.urlopen(url).read().decode()

tokens_sent = sent_tokenize(raw)
tokens = word_tokenize(raw)
textList = Text(tokens)
CONCORD = textList.concordance('brother')
print(CONCORD)
