from nltk import word_tokenize
import string

def tokenization(text):
    tokens = word_tokenize(text)
    # for word in tokens:
    #     if word in string.punctuation:
    #         tokens.remove(word) 
    return tokens

text = "This is a simple sentance. It's a simple task."
print(tokenization(text))