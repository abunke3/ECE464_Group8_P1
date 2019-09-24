def genFaultList(circuit, faultFile, circuitName):
    numFaults = 0
    outFile = open(faultFile, "w")
    
    outFile.write("# " + circuitName + "\n")
    outFile.write("# full SSA fault list\n\n")


    #handles the inputs
    for input in circuit["INPUTS"][1]:
        outFile.write(input[5:] + "-SA-0\n")
        outFile.write(input[5:] + "-SA-1\n")
        numFaults += 2

    for wire in circuit["GATES"][1]:
        outFile.write(wire[5:] + "-SA-0\n")
        outFile.write(wire[5:] + "-SA-1\n")
        numFaults += 2

        for inWire in circuit[wire][1]:
            outFile.write(wire[5:] + "-IN-" + inWire[5:] + "-SA-0\n")
            outFile.write(wire[5:] + "-IN-" + inWire[5:] + "-SA-1\n")
            numFaults += 2

    outFile.write("\n# total faults: " + str(numFaults))