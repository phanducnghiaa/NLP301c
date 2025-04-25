from nltk.tokenize import WordPunctTokenizer
from collections import Counter

def check_common_srating_characters(text: str):
    tokenizer = WordPunctTokenizer()
    tokens = tokenizer.tokenize(text)
    
    filter_tokens = []
    start_words = []

    for word in tokens:
        if word.isalpha():
            filter_tokens.append(word)
            start_words.append(word[0])

    count = Counter(start_words)
    most_common = count.most_common(1)

    # lists_most_common = []

    # for i in count:
    #     if count[i] == most_common[0][1]:
    #         lists_most_common.append(i)
    
    return most_common[0][0]

print(check_common_srating_characters("xin chao viet nam, chao cac ban."))