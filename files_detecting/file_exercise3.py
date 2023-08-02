
#strip will remove the spaces
file_input=open("file_exercise3.txt","r")
for line in file_input:
    data= line.split()  #will remove all the text after index 0 on the right hand side
    print(data[0])
file_input.close()