#write the program to calculate the electricity:
bill=float(input("Enter your bill: "))

if(bill==100):
    print("No charge")
elif(bill ==200):
    print("OR",bill*0.024)
elif(bill>200):
    print("OR", bill*0.047)
    
    