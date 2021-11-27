# To use simply call the file with CPL or BOM
import sys


if len(sys.argv) < 2:
    print('No file to parse, use "' + str(sys.argv[0]) + ' filename.extension"')
    quit()

myFilename = str(sys.argv[2])

if sys.argv[1].lower() == "cpl":
    print("\nComponent placement mode:\n")
    file1 = open(myFilename, 'r')
    Lines = file1.readlines()
     
    count = 0
    # Strips the newline character
    myOutput = ""

    for line in Lines:
        count += 1
        #print("Line{}: {}".format(count, line.strip()))
        if count > 10 :
            myLine = line.strip()
            x = myLine.split()

            partName = x[0]
            partMidX = x[4][1::]
            partMidY = x[5][0:-1:]
            topBottom = "T"

            if len(x) > 6:
                rotation = x[6]
                if rotation[0:1:] == "M":
                    rotation = rotation[2::]
                    topBottom = "B"
                else:
                    rotation = rotation[1::]
            else :
                print("\nLine too short:\n " + myLine + "\n")

            #print(x)
            if x[1] != "DNP" :
                myOutput += partName + ", " + partMidX + ", " + partMidY + ", " + topBottom + ", " + rotation + "\n"
                
    print(myOutput)
    myOutputFilename = myFilename[0:-4:] + "_cpl.csv"

    f = open(myOutputFilename, "w")
    f.write("Designator, Mid X, Mid Y, Layer, Rotation\n")
    f.write(myOutput)
    f.close()

if sys.argv[1].lower() == "bom":   
    print("\nBill of materials mode:\n")
    file1 = open(myFilename, 'r')
    Lines = file1.readlines()
     
    count = 0
    # Strips the newline character
    myOutput = ""

    for line in Lines:
        count += 1
        #print("Line{}: {}".format(count, line.strip()))
        if count > 3 :
            myLine = line.strip()
            x = myLine.split('"')

            #newLine = x[3] + ", " + x[7] + ", " + x[9]
            if x[3] != "DNP" :
                x[9] = x[9].replace(",","")
                myOutput += x[3] + ', ' + x[9] + ', ' + x[7] + " \n"
                
            # print(myOutput)
                
    print(myOutput)
    myOutputFilename = myFilename[0:-4:] + "_bom.csv"

    f = open(myOutputFilename, "w")
    f.write("Comment, Designator, Footprint, JLCPCB Part #\n")
    f.write(myOutput)
    f.close()