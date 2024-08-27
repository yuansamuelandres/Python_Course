# In the name of Allah

import random

def get_choices ():          #indentation is extremely important
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices
choices = get_choices ()
print(choices)

def check_win (player, computer):
    print(f"You chose {player}. Computer chose {computer}")
    if player == computer:
        print("It's a tie")
        # get_choices()
        # check_win(choices["player"], choices["computer"])
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors! You lose."
        else:
            return "Scissors cuts paper! You win!"
result = check_win(choices["player"], choices["computer"])
print(result)

""" Function Arguments
    if Statements
    f Strings
    Accessing Dictionary Values
"""