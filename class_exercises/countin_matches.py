"""#find the first match
found =False #flag
position=0
string="hello p6th7n"
while not found and position < len(string):
    if string[position].isdigit():
        found = True
    else:
        position +=1
if found:
    print(" first digit occuars at position",position)
else:
    print(" the string does not contain a digit ")"""
#reverse
string="hello p6th7n"
found =False #flag
position=len(string)-1

while not found and position >=0:
    if string[position].isdigit():
        found = True
    else:
        position -=1
if found:
    print(" first digit occuars at position",position)
else:
    print(" the string does not contain a digit ")