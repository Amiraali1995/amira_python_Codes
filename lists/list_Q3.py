"""If you have the following list as an input:
[‘red’, ‘yellow’, ‘pink’, ‘black’]
And the following list is the output of it:
[‘red’, ‘purple’, ‘yellow’, ’Black’, ‘green’]
Find how we got the output."""

lis=["red", "yellow", "‘pink’", "‘black’"]
lis.insert(1,"purple")
lis[4]="Black"
lis.pop(3)
lis.append("green")
print(lis)
