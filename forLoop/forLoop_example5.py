# print all numbers from 1 to 100 , if you know that a prefect number is a positive int that equals to the sum of it's,
#positive divisor , excluding the number itself . for instance , 6 divisors 1,2,3 , and 1+2+3=6, 6 is a prefect num

# Find and print perfect numbers from 1 to 100
print("Perfect numbers from 1 to 100:")
for num in range(1, 101):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i

    if divisors_sum == num:
        print(num)
