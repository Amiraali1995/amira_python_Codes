

floor=int(input("Enter floor number: "))

if floor == 13:
    print("Error: there is no thirteen floor")
elif floor <=0 or floor > 20:
    print("Error: floor must be between 1 and 20")

else:

    if floor >13:
        actualFloor = floor - 1
        print("Actual floor ",actualFloor)
    else:
        actualFloor=floor
        print("Actual floor",actualFloor)