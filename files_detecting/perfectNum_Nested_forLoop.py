"""""
3)	Print all perfect number from 1 to 100, if you know that a perfect number is a positive integer that
is equal to the sum of its positive divisors, excluding the number itself. For instance,
6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a perfect number.
"""

for i in range (1,101):
    sum=0
    for j in range(1,i):
        if i%j ==0:
            sum +=j
    if i == sum:
        print(i,"is a perfect number")