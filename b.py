import nltk
from nltk.tokenize import WordPunctTokenizer

text = "Reset your password if you just can't remember your old one."

tokenizer = WordPunctTokenizer()

tokens = tokenizer.tokenize(text)

print(tokens)