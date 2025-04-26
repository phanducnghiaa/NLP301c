def read(filename, output):
    with open(filename, 'r') as file:
        k = []
        text = file.read()
        list_words = text.split()
        print(list_words)

        for word in list_words:
            t = []
            for letter in word:
                if letter.isalpha():
                    t.append(letter)
                else:
                    continue
            k.append("".join(t))

    with open(output, 'w') as outfile:
        for i in k:
            outfile.write(i + " ")

read('punc.txt', 'nopunc.txt')