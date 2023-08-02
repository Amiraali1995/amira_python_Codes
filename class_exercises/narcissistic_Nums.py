"""""
4)	Check whether a number is a Narcissistic number or not in Python, if you know that Narcissistic numbers are the
special type of numbers where that number can be formed by sum of its own digits raised to the power of no. of digits.
"""
# Convert the number to a string to find the number of digits
num = input("Enter the number")
convert_num= int(num)
sum=0

answer=convert_num
while(convert_num!=0):
    digit=convert_num%10
# Calculate the sum of its own digits raised to the power of the number of digits
    sum += digit**(len(num))
    convert_num = convert_num //10
if(sum==answer):
    print("YES")
else:
    print("NO")
