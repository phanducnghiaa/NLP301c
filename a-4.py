from nltk import word_tokenize
import string


def rm_token(text):
    tokens = word_tokenize(text)
    for word in tokens:
        if word.isalpha() and word not in string.punctuation:
            continue
        else:
            tokens.remove(word)

    return tokens


text = "Having lots of fun #goa #vacation #summervacation. Fancy dinner @Beachbay restro"
print(rm_token(text))