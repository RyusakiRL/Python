def char(texts):
    countier = {}

    for letter in texts:
        countier[letter] = countier.get(letter, 0) + 1;

    print(countier)

text = input("Insert the text\n")

char(text)