from nltk import word_tokenize
from nltk.stem import PorterStemmer

root_word = []

def stem_word(text:str):
    text = word_tokenize(text)
    stemmer = PorterStemmer()
    for word in text:
        if word.isalpha():
            root_word.append(stemmer.stem(word))
        else:
            root_word.append(word)
    return root_word

text = 'The cat were playing in the garden, and they were very having fun.'
print(stem_word(text))