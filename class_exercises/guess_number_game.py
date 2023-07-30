import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

while True:
    # Get user's guess as input
    user_guess = int(input("Guess a number between 1 and 100: "))

    # Increment the number of attempts
    attempts += 1

    # Check if the user's guess is correct
    if user_guess == secret_number:
        print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
        break
    elif user_guess < secret_number:
        print("Try again! The number is higher.")
    else:
        print("Try again! The number is lower.")
