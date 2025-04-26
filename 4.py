from gensim.models import Phrases
from nltk import word_tokenize

def create_bigrams(texts):
    tokens = texts.split()
    for idx, char in enumerate(tokens):
        if char.isalpha() == False:
            tokens[idx] = ","

    new_sentence = " ".join(tokens)
    tokens_new = new_sentence.split(",")

    test = []
    for i in tokens_new:
        tokens_new = word_tokenize(i)
        test.append(tokens_new)

    final = []
    pharase = Phrases(test, min_count=1, threshold=1)
    for j in test:
        final.append(pharase[j])

    return final

texts = """The mayor of new york was there "," new york mayor was present"""

result = create_bigrams(texts)

print(result)