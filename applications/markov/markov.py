import random
import re

# Read in all the words in one go
# with open("input.txt") as f:
#     words = f.read()

# TODO: analyze which words can follow other words
# Your code here

fWords = {} # key: word, value: appending words that follow it

def no_dups(s):
    f = open(s, "rt")
    data = f.read()
    # Your code here
    fStrings = []  
 
    
    fStrings = re.split("[ \n]", data)
        
    for i in range(len(fStrings)):
            if i < len(fStrings)-1:
                if fWords.get(fStrings[i]):
                    fWords[fStrings[i]].append(fStrings[i+1])
                else:
                    fWords[fStrings[i]] = [fStrings[i+1]]
            else:
                if fWords.get(fStrings[i]):
                    fWords[fStrings[i]] = fWords[fStrings[i]].append(fStrings[i])
                else:
                    fWords[fStrings[i]] = [fStrings[i]]

no_dups("input.txt")
keys = list(fWords.keys())

print(len(keys))
to_be_removed = []

for i in range(0, len(keys)-1) :
    
    if keys[i] and keys[i][0].islower() and keys[i][0].isalpha(): # and (keys[0] == '"' and keys[-1] != '"' and '.'):
        to_be_removed.append(keys[i])
    elif keys[i] and keys[i][-1] == "." and keys[i][-1] == "!" and keys[i][-1] == "?":
        to_be_removed.append(keys[i])
    else:
        pass


for item in to_be_removed:
    keys.remove(item)

def analyze_word_position(word):
        if word[0] and word[0].isupper() or word[0] == '"': # and word[-2] != '"':
            return (word, 1)
        elif word[-1] == '.' or word[-1] == '?' or word[-1] == '!': # word[-1] == '"': # and word[-2].isalpha() and word[0] != '"':
            return (word,2)
        else:
            return (word, 3)

sentence = [] #NEEDED TO BE GLOBAL BECAUSE THE RECURSIVE NATURE WAS CREATING INDIVIDUAL LISTS

def create_sentences(word):
    wordState = analyze_word_position(word)

    if sentence == [] and wordState[1] == 2:
        pass
    elif sentence == [] and wordState[1] == 1: 
        sentence.append(wordState[0])
        if fWords.get(wordState[0]):
            create_sentences(random.choice(fWords[wordState[0]]))
    elif sentence == [] and wordState[1] == 3:  
        print("Sorry, choose a start word")
    elif sentence != [] and wordState[1] == 2:
        sentence.append(wordState[0])
    else:
        sentence.append(wordState[0])
        if fWords.get(wordState[0]):
            create_sentences(random.choice(fWords[wordState[0]]))





create_sentences(random.choice(keys))
# TODO: construct 5 random sentences
# Your code here

create_sentences(random.choice(keys))
create_sentences(random.choice(keys))
create_sentences(random.choice(keys))
create_sentences(random.choice(keys))
create_sentences(random.choice(keys))
print(" ".join(sentence))