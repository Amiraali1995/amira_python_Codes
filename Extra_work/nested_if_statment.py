userinput=int(input("Enter a number"))

if userinput >=0:
    if userinput %3==0:
        print("your number is positive and divisiable by 3")
    else:
        print("your number is positive but not divisiable by 3")
else:
    print("your number is negative")
