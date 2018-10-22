#MAPPING SENTENCES TO LIBRARY
import json

#declare trainData as an empty list
trainData = []

with open("Consolidated_data.txt","r") as f:
    
    #temp list for each sentence
    tempList = []
    
    #read data-file line by line
    for line in f:
        #set tempList to empty for each new line
        del tempList[:]
        #find "sentence":" index
        temp = line.find("\"sentence\":\"")
        
        #substring from index of first quotation char in "sentence":" +12
        #to the end, not including last 3 characters, which are "})
        #lowercase all characters
        newLine = (line[(temp+12):-4]).lower()
        
        #delete all unnecessary characters and spaces from a string
        newLine = newLine.translate(None, '.,-\":;~!@#$%^&?[]{}<>`1234567890\\*()').strip()
        
        
        #load library
        with open("library.json", "r") as l:
            data = json.load(l)
            
            #split each line into array of separate words
            for x in newLine.split(' '):
                #if the word in the library, append it to tempList
                if x in data:
                    tempList.append(data[x])
            #after all words mapped to the library, append tempList to trainData
            trainData.append(tempList[:])