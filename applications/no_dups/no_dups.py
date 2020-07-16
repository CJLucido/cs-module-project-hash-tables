def no_dups(s):
    # Your code here
    fStrings = []  
    fWords = []

    for fLine in s:
        fStrings.append(fLine)

    for fLineHere in fStrings:
        for character in fLineHere:
            if character.isalpha():
                character.lower()

        fLineHere.split() #flinehere now a list
        for i in fLineHere:
            if i in fWords:
                pass
            else:
                fWords.append(i)

    print(" ".join(fWords))


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))