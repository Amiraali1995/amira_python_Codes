from  sys import exit

mark=float(input("Enter mark:"))
if mark <0 or mark >100:
    exit("Error: You mist enter a mark between 0 and 100")
if mark >= 90:
    grade="A"
elif mark >=80:
    grade="B"
elif mark >=70:
    grade="C"
elif mark >=60:
    grade="D"
else:
    grade="F"
print("Your grade is: ",grade)