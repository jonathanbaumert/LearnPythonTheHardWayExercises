from sys import argv
from os.path import exists

script, fromFile, toFile = argv
print(f"Copying from {fromFile} to {toFile}")

# we could do these two on one line, how?
inFile = open(fromFile)
indata = inFile.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(toFile)}")
print("Read, hit RETURN to continue, CTRL-Z to abort")
input()

outFile = open(toFile,'w')
outFile.write(indata)

print("Alright, all done.")

outFile.close()
inFile.close()