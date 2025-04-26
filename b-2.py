def longest_word(text):
    len_index = []
    words_list = text.split()

    for word in words_list:
        len_index.append(len(word))

    for lenght, letter in zip(len_index, words_list):
        if lenght == max(len_index):
            return letter
                
text = "Python is a high-level programming programming language"
longest_word(text)
print(longest_word(text))