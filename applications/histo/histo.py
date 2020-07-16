# Your code here




    


def print_sorted_numerical(wordCount):#may have to move above

    wordCountSorted = list(wordCount.items())
    # print(characters)
    # print(characters.sort())
    wordCountSorted.sort(key=lambda pair: pair[1], reverse=True)
    
    for word in wordCountSorted:
        wordCountSorted[word] = wordCountSorted[word] * "#"
  
    
    wordCountSorted[0] =  wordCountSorted[0] + "  "
    
    for pair in wordCountSorted:
        print(f'{pair[0]}:{pair[1]}')

def print_sorted_alpha(wordCount):
    wordCountSorted = list(wordCount.items())
    # print(characters)
    # print(characters.sort())
    wordCountSorted.sort(key=lambda pair: pair[0], reverse=True)
    
    for word in wordCountSorted:
        wordCountSorted[word] = wordCountSorted[word] * "#"
  
    
    wordCountSorted[0] =  wordCountSorted[0] + "  "
    
    for pair in wordCountSorted:
        print(f'{pair[0]}:{pair[1]}')


def histo(file):
    fStrings = []  
    fWordCounts = {}

    f = open(file, "rt")

    for fLine in f:
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


    
    print_sorted_numerical(fWordCounts)
    print_sorted_alpha(fWordCounts)



histo("robin.txt")