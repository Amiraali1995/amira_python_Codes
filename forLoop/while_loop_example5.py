
#generate two  random numbers range from 1 to 100
#the program will add these two numbers and ask the user the answer of sum of those two numbers
# check  if the answer is correct or wrong
#the program will keep repeat asking the user to answer until the user type done then the loop will end

import random





# Calculate the correct sum
#correct_sum = random.randint(1, 100) + random.randint(1, 100)

while 1:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print("Question:", f"{num1} + {num2}", " ?")
    user_answer = input("Add the following two numbers:")
    # Calculate the correct sum
    correct_sum = num1 + num2

    if((user_answer) != "done"):
        if(int(user_answer) == correct_sum):
            print(" Your answer is correct.")

        else:
            print("your answer is wrong. Please try again.")
    else:
        break




