# we are creating a game where the user has to choose one of three elements, rock, paper or scissors
# the computer will also choose one of the three elements
# if the user beats the computer, they get one point and vice versa
# if the user and the computer choose the same element, it is a draw
# paper beats rock, rock beats scissors, scissors beats paper
# the user will be told if they won or lost
# the user will be able to play again or quit
# the user will be able to see their score
# the game interaction will happen in the terminal 

import random
import sys

print("Welcome to Rock, Paper, Scissors!")
print("Enter 'q' to quit the game")

options = ["rock", "paper", "scissors"]
score = 0

while True:
    user_choice = input("Enter rock, paper or scissors: ")
    if user_choice == "q":
        print("Goodbye!")
        sys.exit()
    if user_choice not in options:
        print("Invalid choice. Please try again")
        continue
    computer_choice = random.choice(options)
    print(f"Computer chose {computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        score += 1
    else:
        print("You lose!")
    print(f"Score: {score}")
    play_again = input("Do you want to play again? (y/n): ")
    if play_again != "y":
        print("Goodbye!")
        sys.exit()