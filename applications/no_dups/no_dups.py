def no_dups(s):
    # Your code here
    fStrings = []  
    fWords = []

    fStrings = s.split(" ")
    
    for i in fStrings:
        if i in fWords:
            pass
        else:
            fWords.append(i)

    return " ".join(fWords)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))