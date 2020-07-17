# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

fStrings = []    
fChars = {}
mostFreq = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']


f = open("ciphertext.txt", "rt")

for fLine in f:
    fStrings.append(fLine)

for fLineHere in fStrings:
    for character in fLineHere:
        if character.isalpha():
            if character in fChars:
                fChars[character] +=1
            else:
                fChars[character] = 1

def sum_total_char():
    char_sorted = list(fChars.items())
    # print(characters)
    # print(characters.sort())
    char_sorted.sort(key=lambda pair: pair[1], reverse=True)
 
    sum_total = 0
    list_percentages = {}
    new_list = []
    
    for pair in char_sorted:
        sum_total += sum_total + pair[1]

    for pair in char_sorted:
        print(f'Letter: {pair[0]}, count: {pair[1]}')
        if pair[0] not in list_percentages:
            list_percentages[pair[0]] = (pair[1] / sum_total)*100
        else:
            pass
    i = 0
    for pair in char_sorted:
        new_list.append(list(pair))
    print(new_list)
    for pair in new_list:
        
        if i < len(mostFreq):
            pair[1] = mostFreq[i]
            i+= 1
            print(new_list)
        else:
            pass
    del new_list[-1]
    decode_txt(new_list)
    


def decode_txt(char_sorted):
    # for fLineHere in fStrings:
    #     for k in range(len(fLineHere)):
    #         #print(fLineHere[k])
    #         letterToChange = fLineHere[k]
    #         letterToUse= fLineHere[k]
    #         for pair in char_sorted:
    #             if pair[0] == letterToChange:
    #                 letterToUse = pair[1]
    #             else:
    #                 continue
    #         #print(letterToChange)
            
    #         fLineHere[k] = fLineHere.replace(letterToChange, letterToUse)
    #         print(fLineHere)
          
    # print(fStrings)
    
    f = open("ciphertext copy.txt", "rt")
    # fout = open('output.txt', "wt")
    data = f.read()

    for k in range(len(data)):

        letterToChange = data[k]
                
        letterToUse= data[k]
        for pair in char_sorted:
                if pair[0] == letterToChange:
                    letterToUse = pair[1]
                else:
                    continue

                new_data = data[:k] + letterToUse + data[k+1:]
                # data.replace(letterToChange,letterToUse) ##no good because strings are immutable!
                data = new_data
           
    print(data)
    f.close()  

    f = open("ciphertextcopy.txt", "w")
    f.write(data)
    f.close()
    # fout.close() 

sum_total_char()
