def print_words(wordCount):#may have to move above

    wordCountSorted = list(wordCount.items())
    # print(characters)
    # print(characters.sort())
    # wordCountSorted.sort(key=lambda pair: pair[1], reverse=True)
    
    for pair in wordCountSorted:
        print(f'{pair[0]}:{pair[1]}')

def word_count(s):
    # Your code here
    fStrings = []  
    fWordCounts = {}

    for fLine in s:
        fStrings.append(fLine)

    for fLineHere in fStrings:
        for character in fLineHere:
            if character.isalpha():
                character.lower()

        fLineHere.split() #flinehere now a list
        for i in fLineHere:
            if i in fWordCounts:
                fWordCounts[i] += 1
            else:
                fWordCounts[i] = 1
    print_words(fWordCounts)


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))