
negative=0
inputStr=input("Enter a value:")
while inputStr !="":
    value=float(inputStr)
    if value<0:
        negative+=1

    inputStr=input("Enter a value: ")
print("There were", negative,"negative values")




"""
total=0.0
count=0
inputStr=input("Enter a value")
while inputStr !="":
    value=float(inputStr)
    total+=value
    count+=1
    inputStr=input("Enter a value: ")
    if count > 0:
        average = total / count
    else:
        average = 0.0"""
