import re

def print_words(wordCount):#may have to move above

    wordCountSorted = list(wordCount.items())
    # print(characters)
    # print(characters.sort())
    # wordCountSorted.sort(key=lambda pair: pair[1], reverse=True)
    
    for pair in wordCountSorted:
        print(f'{pair[0]}:{pair[1]}')

def remove_ignored(word):
    for character in word:
        if character in '":;,.-+=/\|[]{ }()*^&':
           word = word.replace(character, "")
        else:
            pass
    # print(word)
    return word

def word_count(s):
    # Your code here
    fStrings = []  
    fWordCounts = {}
    if len(s) <= 0:
        return {}
    else:
        # fStrings = s.split(" ")
        
        fStrings = re.split("[\*|\n| |\t|\r]", s)
        
        fStrings = list(map(remove_ignored, fStrings))
        # print(fStrings)
        # for word in fStrings:
            # for character in word:
                
                # fStrings[character] = character.lower()
        fStrings = list(map(str.lower, fStrings))
        # print(fStrings)
            # fLineHere.split() #flinehere now a list
        for i in fStrings:
                if i in fWordCounts and i != "":
                    fWordCounts[i] += 1
                elif i != "":
                    fWordCounts[i] = 1

        print(fWordCounts)
        return fWordCounts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))