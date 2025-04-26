from nltk import word_tokenize, pos_tag

def verb_pharse(text):
    verb_pharses_list = []
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    for index, (word, tag) in enumerate(tagged):
        if tag.startswith('VB'):
            if tagged[index - 1][1] == 'MD':
                verb_pharses_list.append(tagged[index - 1][0] + ' ' + word)
            elif tagged[index - 1][1] == 'TO':
                if tagged[index - 2][1] == 'VB':
                    verb_pharses_list.append(tagged[index - 2][0] + ' ' + tagged[index - 1][0] + ' ' + word)
                elif tagged[index - 3][1] == 'VB':
                    verb_pharses_list.append(tagged[index - 3][0] + ' ' + tagged[index - 2][0] + ' ' + tagged[index - 1][0] + ' ' + word)


    return verb_pharses_list

text = "I may bake a cake for my birthday. The talk will introduce reader about Use of baking."
print(verb_pharse(text))