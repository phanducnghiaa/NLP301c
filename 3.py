from nltk import word_tokenize, pos_tag

def extract_verb_phrases(text):
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    # print(pos_tags)
    pharse_verb = []
    
    for idx, (word, tag) in enumerate(pos_tags):
        if tag.startswith('VB'):
            if pos_tags[idx-1][1] == 'MD':
                pharse_verb.append(f"{pos_tags[idx-1][0]} {word}")
            elif pos_tags[idx-1][1] == 'TO':
                if pos_tags[idx-2][1].startswith('VB'):
                    pharse_verb.append(f"{pos_tags[idx-2][0]} {pos_tags[idx-1][0]} {word}")
                elif pos_tags[idx-3][1].startswith('VB'):
                    pharse_verb.append(f"{pos_tags[idx-3][0]} {pos_tags[idx-2][0]} {pos_tags[idx-1][0]} {word}")
    return pharse_verb

text = "I may bake a cake for my birthday. The talk will introduce reader about Use of baking. have to do. Be able to do"

result = extract_verb_phrases(text)


print(result)