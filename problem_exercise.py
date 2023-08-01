#write a python program that go throw all numbers from 1 to 30 and print true if the number is prime false if not .
#the out put format should be like the' following


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

for num in range(1, 31):
    print(num, is_prime(num))
