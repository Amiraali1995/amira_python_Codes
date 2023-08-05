#This program simulates an elevator panel that skips the 13th floor

#obtain the floor number from the user as an input
floor=int(input("Enter the floor number:"))

#Adjust floor if nescessary
if floor >13:
    actualFloor=floor-1
else:
    actualFloor=floor
#print the result:
print("The elevator will travel to the actual floor :",actualFloor)
