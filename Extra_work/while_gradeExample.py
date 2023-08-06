numPassing=0
numFailing=0

total=0
count=0
minGrade=100.0
maxGrade=0.0

grade=float(input("Enter a grade or -1 to finish: "))
while grade >= 0.0:
    if grade >=60.0:
        numPassing=numPassing+1
    else:
        numFailing=numFailing+1

    if grade< minGrade:
        minGrade=grade
    else:
        maxGrade=grade

    total = total +grade
    count = count+1
    grade =float(input("Enter a grade or -1 to finish: "))
if count >0:
    average=total/count
    print("The average grade is %.2f"%average)
    print("The passing grade is " ,numPassing)
    print("The failing grade is ", numFailing)
    print("The maximum grade is %.2f" % maxGrade)
    print("The minimum grade is %.2f" % minGrade)