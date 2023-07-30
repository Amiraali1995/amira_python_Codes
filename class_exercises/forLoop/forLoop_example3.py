#for i in range(1,6):
#    print(i ,end=" ")
#output:1 2 3 4 5

#************************************************************
"""""
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
"""
#*************************************************************
#another way same output

n=6

for i in range(1,6):
    for i in range(1,n):
        print(i, end=" ")
    print(" ")
    n -=1

"""""
output:
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
"""
