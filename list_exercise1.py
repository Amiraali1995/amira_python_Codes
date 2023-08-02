#write a for loop that iterate over the ements of mylist for computing the sum of all elements in a list

#*****************************************************************
#using list index
myList = [1, 2, 3, 4, 5]
sum=0
for i in range(len(myList)):
    sum += myList[i]
print("Another way to sum all the elements is list",sum)
#********************************************************************
#calculate elements of mylist using element
sum=0
for element in myList:
    sum+=element
    print()
print("Another way calculate elements of mylist using element",sum)
#*********************************************************************
#without using for loop
myList = [1, 2, 3, 4, 5]
sum_of_numbers = sum(myList)

print("The sum of the numbers in list:", sum_of_numbers)

