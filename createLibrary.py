import json

#data = open("Consolidated_data.txt","r") 
with open("Consolidated_data.txt","r") as f:
    
    #declare library as an empty list
    library = []
    
    #read data-file line by line
    for line in f:
        
        #find "sentence":" index
        temp = line.find("\"sentence\":\"")
        
        #substring from index of first quotation char in "sentence":" +12
        #to the end, not including last 3 characters, which are "})
        #lowercase all characters
        newLine = (line[(temp+12):-4]).lower()
        
        #delete all unnecessary characters from a string
        newLine = newLine.translate(None, '.,-\":;~!@#$%^&?[]{}<>`1234567890\\*()')
        
        #for each element in newLine array, splitted at space
        for x in newLine.split(' '):
            #if the element is not in the library, add it
            if (x not in library):
                library.append(x)
        
    #JSON string of library
    libraryJSON = "{"
    for index, value in enumerate(library):
        #take care of trailing comma
        if index != len(library)-1:
            libraryJSON += "\"" + value + "\"" + ': ' + str(index) + ", "
        else:
            libraryJSON += "\"" + value + "\"" + ': ' + str(index)
    
    libraryJSON += "}"
    
    #create file for libraryJSON string
    with open('library.json', 'w+') as l:
        l.write(libraryJSON)