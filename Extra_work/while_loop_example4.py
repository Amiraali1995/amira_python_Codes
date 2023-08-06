salary=0.0
count=0
total=0
while salary >=0:
    salary =float(input("Enter a salary or -1 to finish:"))
    if salary >=0.0:
        total+=salary
        count=count+1
if count>0:
    average=total/count
    print("Average salary is: ",average)
else:
    print("No data was entered")