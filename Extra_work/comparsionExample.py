x = float(input("Enter a number such as (3.5 or 4.5)"))
y = float(input("Enter a  second number "))

if x == y:
    print("They are the same number")
else:
    if x > y:
        print("The first number is larger")
    else:
        print("The first number is smaller")
    if -0.01 < x -y and x- y < 0.01:
        print("The number are close together ")
    if x ==y+1 or x==y-1:
        print("The numbers are one part")
    if x >0 and y>0 or x <0 and y<0:
        print("The numbers have the same signs ")
    else:
        print("The numbers have different signs")