from nltk.stem import PorterStemmer
from nltk import word_tokenize

def stem_word(text:str):
    stem_words = []
    tokens = word_tokenize(text)
    stemmer = PorterStemmer()
    for word in tokens:
        if word.isalpha():
            # if "e" == word[-2] and word[-1] == "r":
            #     if "e" == word[-2] and word[-1] == "r" and word[-3] == word[-4]:
            #         word = word[:-3]
            #         stem_words.append(word)
            #     else:
            #         word = word[:-2]
            #         stem_words.append(word)
            # else:
                stem_words.append(stemmer.stem(word))
        else:
            continue
    return stem_words

text = 'running runs runner'
print(stem_word(text))

print("runner"[-1:-3])