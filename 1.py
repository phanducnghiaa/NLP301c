from nltk.tokenize import WordPunctTokenizer
from nltk.stem import PorterStemmer
from nltk import word_tokenize

original_text = []

def a(text):
    tokenizer = WordPunctTokenizer()
    tokens = tokenizer.tokenize(text)
    stemmer = PorterStemmer()
    for words in tokens:
        original_text.append(stemmer.stem(words))
    return original_text

print(a("The cat were play in the garden, and they were having fun."))


def b(text):
    original_text_2 = []
    tokens = word_tokenize(text)
    stemmer = PorterStemmer()
    for words in tokens:
        original_text_2.append(stemmer.stem(words))
    return original_text_2

print(b("The cat were play in the garden, and they were having fun."))