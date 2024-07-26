"""
Rock, Paper, and Scissor
"""


from random import choice


def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    user = input("Make your move (rock, paper or scissors): ")
    computer_choice = choice(choices)
    print("The move of the computer (rock, paper or scissors): ", computer_choice)

    if user == computer_choice:
        print("Draw")
    elif user == "paper" and computer_choice == "rock":
        print("User Won!")
    elif user == "rock" and computer_choice == "scissors":
        print("User Won!")
    elif user == "scissors" and computer_choice == "paper":
        print("User Won!")
    else:
        print("Computer Won")

rock_paper_scissors()