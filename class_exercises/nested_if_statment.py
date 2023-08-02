#nested_if statment
state=input("are you graduated enter(Y/N)").upper()
age=int(input("Enter you age"))
if (age >= 18):
    if(state =='Y'):
        print("graduated and 18 or above years old")
    else:
         print("Not graduated and 18 or above years old")
else:
     print("under 18 years old")
