# Problem 8
# Sang Park

import random

def get_user_choice():
    choice = input("Please choose 'paper', 'rock', or 'scissors': ").lower()
    while choice not in ["paper", "rock", "scissors"]:
        return choice 
    return choice

while True:
    computer_object = random.choice(["paper", "rock", "scissors"])
    user_object = get_user_choice()

    if user_object == computer_object:
        print("The objects are the same, play again!")
        continue  
    
    print(f"You chose: {user_object}")
    print(f"Computer chose: {computer_object}")

    if (user_object == "rock" and computer_object == "scissors") or \
       (user_object == "scissors" and computer_object == "paper") or \
       (user_object == "paper" and computer_object == "rock"):
        print("You win!")
    else:
        print("The computer wins :(")

    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again == 'n':
        print("Thanks for playing!")
        break  
