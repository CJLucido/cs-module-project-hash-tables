# Your code here

def print_sorted_numerical(wordCount):#may have to move above

    wordCountSorted = list(wordCount.items())
    wordCountSorted.sort(key=lambda pair: pair[1], reverse=True)
    wordCountHashMark = []
    for pair in wordCountSorted:
        if pair == wordCountSorted[0]:
            wordCountHashMark.append((pair[0],"  " + (pair[1]*"#")))
        else:
            wordCountHashMark.append((pair[0],pair[1]*"#"))
    
    for pair in wordCountHashMark:
        print(f'{pair[0]}:{pair[1]}')

def print_sorted_alpha(wordCount):
    wordCountSorted = list(wordCount.items())
    wordCountSorted.sort(key=lambda pair: pair[0])
    wordCountAlpha = []
    for pair in wordCountSorted:
        if pair == wordCountSorted[0]:
           wordCountAlpha.append((pair[0],"  " + (pair[1]*"#"))) 
        else: 
            wordCountAlpha.append((pair[0],pair[1]*"#"))

    for pair in wordCountAlpha:
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
            if i.isalpha() and not i.isupper():
                if i in fWordCounts:
                    fWordCounts[i] += 1
                else:
                    fWordCounts[i] = 1
            else:
                pass


    
    print_sorted_numerical(fWordCounts)
    print_sorted_alpha(fWordCounts)



histo("robin.txt")