numExam=int(input("How many exam greads does each student have? "))
moreGreades='Y'
while moreGreades =='Y':
    print("Enter the exam greades.")
    total=0
    for i in range(1,numExam+1):
        score=int(input("Exam %d:"%i))
        total=total+score
    average=total/numExam
    print("The average is %.2f"%average)

    moreGreades=input("Enter exam greades for another student (Y/N)? ")
    moreGreades=moreGreades.upper()