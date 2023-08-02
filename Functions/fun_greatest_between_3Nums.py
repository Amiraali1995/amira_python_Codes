
a=int(input("Enter the value of A: "))
b=int(input("Enter the value of B: "))
c=int(input("Enter the value of C: "))

def get_max_num(a,b,c):
    if a>= b and a>=c:
        return  a
    elif b>= a and b>=c:
        return b
    else:
        return c
max_num=get_max_num(a,b,c)
print("The Maximum number is ",max_num)


