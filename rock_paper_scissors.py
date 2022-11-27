#first import the random module so the computer chooses a random choice
import random

while True:
#create a list of choices
    choices = ["rock", "paper", "scissors"]
#assign a random choice to the computer
    computer = random.choice(choices)
    player =  None
#player must input their choice
    while player not in choices:
        player = input("Choose rock, paper, or scissors:").lower()

#win conditions
    if player == computer:
        print("computer chose: ", computer)
        print("you chose: ", player)
        print("Tie!")
    elif player == "rock" and computer == "scissors":
        print("computer chose: ", computer)
        print("you chose: ", player)
        print("You win!")
    elif player == "rock" and computer == "paper":
        print("computer chose: ", computer)
        print("you chose: ", player)
        print("You lose!")
    elif player == "paper" and computer == "rock":
        print("computer chose: ", computer)
        print("you chose: ", player)
        print("You win!")
    elif player == "paper" and computer == "scissors":
        print("computer chose: ", computer)
        print("you chose: ", player)
        print("You lose!")
    elif player == "scissors" and computer == "paper":
        print("computer chose: ", computer)
        print("you chose: ", player)
        print("You win!")
    elif player == "scissors" and computer == "rock":
        print("computer chose: ", computer)
        print("you chose: ", player)
        print("You lose!")

#ask the player if they want to play again
    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y":
        break

print("Thanks for playing!")
