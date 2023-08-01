#linesr search of list
my_list=[10,20,30,90]
limit=90
pos=0
found=False
while pos < len(my_list) and not found:
    if my_list[pos] == limit:
        found =True
    else:
        pos +=1
if found:
    print("fond at position",pos)
else:
    print("Not found ")
