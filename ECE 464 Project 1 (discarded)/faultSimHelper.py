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


#faults=faults list
#index=line number 
#elif (faults[index][1][1]=='IN')
def faultAnalyze(faults, index):
    #print(faults[index][1][1]=='SA')
    #fSignal='0'
    #fWire='1'

    if faults[index][1][1]=='SA': #Wire SA fault
        fSignal=faults[index][1][2] #the signal the wire is stuck at
        #tx=faults[index][1][0].lower()
        tx=faults[index][1][0]
        fWireX='wire_'+ tx #the wire we are focusing on
        fWireY='' #only needed for X-IN-Y faults
    else:    # X IN Y fault
        fSignal=faults[index][1][4]#the signal the wire is stuck at
        #tx=faults[index][1][0].lower()
        #ty=faults[index][1][2].lower()
        tx=faults[index][1][0]
        ty=faults[index][1][2]
        fWireX='wire_'+ tx #wire x
        fWireY='wire_'+ ty #wire y


    return [fSignal, fWireX, fWireY]



def indexSwap(tempList, wireMatch):
    length=len(tempList)
    for i in range(length):
        if wireMatch==tempList[i]:
            break
    return i

def faultCompare():



    return -1
