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
    print(" the string does not contain a digit ")