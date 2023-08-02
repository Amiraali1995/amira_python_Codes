weight=float(input("Enter you weight: "))

height=float(input("Enter you height: "))
BMI= weight/(height*100)**2
if(BMI<18.5):
    print("Under weight")
elif(18.5<= BMI<25.0):
    print("Normal")
elif(25.0<= BMI<30.0):
    print("Over weight")
elif(30.0<= BMI):
    print("obese")