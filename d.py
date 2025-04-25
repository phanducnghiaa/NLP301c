from nltk.tokenize import WordPunctTokenizer 

tokens_list = []

def a(text,string):
    tokenizer = WordPunctTokenizer()
    tokens = tokenizer.tokenize(text)
    for words in tokens:
        if words.isalpha():
            tokens_list.append(words)
    count = 0
    for i in tokens_list:
        if string in i:
            count += 1
        else:
            continue

    total = count / len(tokens_list) * 100        
    print(total)

a("xin chao viet nam, chao cac ban", "ao")