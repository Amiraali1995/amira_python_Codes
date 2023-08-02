"""""
Mohamed will give you two integers a and b, and you will be required to find the greatest common factor between them; Where is the common factor
The largest of the two numbers a and b is the largest factor or divisor between the two numbers in common.
Example: If Muhammad has the numbers 10 and 15, then:
The divisors of the number 10 are: 1 - 2 - 5 - 10.
The divisors of the number 15 are: 1 - 3 - 5 - 15.
So, the greatest common divisor of both numbers is 5
"""
import math
fist_num=int(input("Enter the first number: "))
second_num=int(input("Enter the second number: "))
print("The GCD of",fist_num,second_num)
print(math.gcd(fist_num,second_num),"is the greatest factor or denominator among common denominators")

