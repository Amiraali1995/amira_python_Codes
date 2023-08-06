value=int(input("Enter a value:"))
inputStr=input("Enter a value:")
while inputStr !="":
    previous=value
    value=int(inputStr)

    if value==previous:
        print("Duplicated input")

    inputStr=input("Enter a value: ")