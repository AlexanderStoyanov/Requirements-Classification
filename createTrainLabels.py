#SEPARATION OF REQUIREMENTS INTO FUNCTIONAL AND NON-FUNCTIONAL

#declare trainLabels as an empty list
trainLabels = []

with open("Consolidated_data.txt","r") as f:
    i = 0
    for line in f:
        
        #find where class begins
        front = line.find("\"class\":\"")
        
        #find where class ends (where sentence begins)
        end = line.find("\",\"sentence\":\"")
        
        #substring line based on front and end above
        reqClass = (line[(front+9):end]).lower()
        if "nonfunctional" in reqClass:
            trainLabels.append(0)
        elif "functional" not in reqClass:
            trainLabels.append(0)
        else:
            i+=1
            trainLabels.append(1)
        
print trainLabels
print "There are " + str(len(trainLabels)) + " requirement statements"
print "Of which " + str(i) + " are functional"
print "And " + str(len(trainLabels)-i) + " are nonfunctional"