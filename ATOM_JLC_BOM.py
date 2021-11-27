#EXPORT BOM in EAGLECAD
#CHOOSE VALUES and CSV

import sys


if len(sys.argv) < 2:
    print('No file to parse, use "' + str(sys.argv[0]) + ' filename.csv"')
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
    if count > 3 :
        myLine = line.strip()
        x = myLine.split('"')

        #newLine = x[3] + ", " + x[7] + ", " + x[9]
        if x[3] != "DNP" :
            x[9] = x[9].replace(",","")
            myOutput += x[3] + ', ' + x[9] + ', ' + x[7] + " \n"
            
            #print(myOutput)
            
print(myOutput)
myOutputFilename = myFilename[0:-4:] + "_bom.csv"

f = open(myOutputFilename, "w")
f.write("Comment, Designator, Footprint, JLCPCB Part #\n")
f.write(myOutput)
f.close()