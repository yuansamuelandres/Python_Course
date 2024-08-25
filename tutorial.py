# In the name of Allah

import random

def get_choices():          #indentation is extremely important
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices
choices = get_choices()

def greeting():
    return "Hi"
response = greeting()
print(response)

print(choices)


""" Variables, 
    Functions, 
    Dictionaries,
    Libraries & Methods,  
    Lists
"""