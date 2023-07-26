#exercise 4
gander=input("Enter gander (F/M)").upper()
age=int(input("Enter you age"))

if(age >= 25 and age <= 30):
    if(gander=='M'):
        print("Your accepted")
    else:
        print(" rejected , your female")
else:
     print("Your rejected")
