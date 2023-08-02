t=(("a","b")*10) #
print(t)
"""
t1=(1,2)
t1[1]=3
print(t1) # returns error because the tuple is immutable (unchangable)"""
#******************************************************************************************
print("-"*100)
t4=((1,2,3),("a","b","c"))
for j in t4:
    for k in j:
        print(k,end="")
    print()
#output: 123
#        abc
print("-"*100)