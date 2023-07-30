
#generate two  random numbers range from 1 to 100
#the program will add these two numbers and ask the user the answer of sum of those two numbers
# check  if the answer is correct or wrong

import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

#print("Add the following two numbers:")

print("Question:",f"{num1} + {num2}"," ?")
user_answer = int(input("Add the following two numbers:"))
# Calculate the correct sum
correct_sum = num1 + num2

# Calculate the correct sum
#correct_sum = random.randint(1, 100) + random.randint(1, 100)

if (user_answer==correct_sum):
    while user_answer == correct_sum:
        print(" Your answer is correct.")
        user_answer = int(input())

    print("your answer is wrong. Please try again.")