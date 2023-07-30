#1729 user will input this number
#then we need add those numbers 1+7+2+9
#1729 === output will be 19 => 1+7+2+9= 19
#input : 123 =out will be 6 => 1+2+3


n = int(input("Enter a number"))
total= 0
while(n>0):
    digit = n % 10
    total += digit
    n = n // 10