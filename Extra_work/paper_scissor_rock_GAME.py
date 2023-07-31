import random
#pick any random choice
#paper,scissor,rock game
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None
    # print(computer)
    while player not in choices:  # if you type something that is not in the list  the loop will keep asking until you type the correct chice that is in the list
        player = input(
            "rock, paper, or scissors?: ").lower()  # will someone will type capital letter out will not show so we have to write lower()

    if player == computer:  # if the both get the same answer
        print("Computer: ", computer)
        print("Player: ", player)
        print("Tie!")
    elif player == "rock":  # if the player picks rock then check who is the winner
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
    elif player == "scissors":  # if the player picks scissors and check who will win or lose
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
    elif player == "paper":  # if the player picks paper and check who will win or lose
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")

    play_again = input("Play Again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye!")

