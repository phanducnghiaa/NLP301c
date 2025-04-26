from nltk import word_tokenize
from nltk.probability import FreqDist
import string

sentance_list = []
dict_word = dict()

def count_frequency_words(text):
    for word in text.split():
        if word in string.punctuation:
            word.remove(word)
        else:
            sentance_list.append(word)

    freq_dist = FreqDist(sentance_list)
    freq_dist.most_common()
    for word, freq in freq_dist.items():
        dict_word.update({word: freq})
    return dict_word

print(count_frequency_words("This is a semple text. This text is for testing purpose."))
            