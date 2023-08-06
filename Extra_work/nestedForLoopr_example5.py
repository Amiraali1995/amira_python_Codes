#the table prints a table pf powers x

nmax=4
#xmax=10
xmax=4
#print table header
for n in range(1,nmax+1):
    print("%10d"%n,end="")
print()
for n in range(1,nmax+1):
    print("%10s" % "x", end="")
print("\n" ,"   ","-"*35)

#print table body

for x in range(1,xmax+1):
    for n in range(1, nmax + 1):
        print("%10.0f"%x**n,end="")
    print()