# Q03a

import re

#	Open the file and input data

emailFile = open("Email.txt", "r+")

#	Open output file
outputFile = open("Error.txt","w+")

#	Find errors and write to output file
for line in emailFile:
    # print(line)
    if not re.search("@", line):
        outputFile.write(f'{line} \n')

#	Close files

