#File detecting
"""
file mood
*read
*write
*append
"""

"""" 
#will read only one line 
input_file=open("infile.txt","r") #text file with read mood
line=input_file.readline() # will the first line in infile.txt
print(line) #print line that will read the first line in infile.txt 
"""

#will read will all the lines in the infile.txt
input_file=open("infile.txt","r") #text file with read mood
for line in input_file:
    if int(line) %2 == 0:         #to print the even numbers 
        print(line)


