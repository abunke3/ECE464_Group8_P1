from pprint import pprint

def getFaults(faultFile):
    #opens the file
    inFile = open(faultFile, "r")

    faults = []

    #goes line by line and adds the faults to arrays
    for line in inFile:
        # Do nothing else if empty lines, ...
        if (line == "\n"):
            continue
        # ... or any comments
        if (line[0] == "#"):
            continue
        
        line = line.replace("\n", "")
        data = [False]
        data.append(line.split("-"))

        faults.append(data)
    
    return faults