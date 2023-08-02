"""
exercise2.txt
678
123
591

"""
input_file=open("exercise2.txt","r")
for line in input_file:
    print(line[0])