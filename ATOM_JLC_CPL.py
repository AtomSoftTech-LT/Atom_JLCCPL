import sys


if len(sys.argv) < 2:
    print('No file to parse, use "' + str(sys.argv[0]) + ' filename.extension"')
    quit()


myFilename = str(sys.argv[1])

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