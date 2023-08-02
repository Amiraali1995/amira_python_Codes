"""Given the definition
Values = [0, 0, 0, 0, 0, 0, 0]
Write statements to put the integer 10 into the elements of list values with
the lowest and the highest valid index."""
values = [0, 0, 0, 0, 0, 0, 0]
# Put the integer 10 into the element with the lowest valid index (index 0)
values[0]=10
# Put the integer 10 into the element with the highest valid index (index 6)
values[-1]=10   # or another way values[6]=10
print(values)

