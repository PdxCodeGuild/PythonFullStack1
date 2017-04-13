"""This is the module level Docstring..."""

import random

computer_choice = random.randint(1, 10)


correct = False

while correct == False:

    human_guess = int(input('What is your guess?'))

    if human_guess < computer_choice:
        print("Too low...")
    elif human_guess > computer_choice:
        print("Too high...")
    elif human_guess == computer_choice:
        print("Correct Guess!")
        correct = True
