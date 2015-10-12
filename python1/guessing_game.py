#!/usr/local/bin/python3
#
# Guessing Game
# guessing_game.py
#
# 2015 June 28th
#
""" Prompts the user to guess a number between 1 and 99. """
import random

number_to_guess = random.randint(0, 99)

while True:
    guess = input("Guess a number: ").strip()
    if not guess.isdigit():
        print("Please enter a number.")
        continue
    
    if int(guess) == number_to_guess:
        print("You guessed it!")
        break
    
    elif int(guess) > number_to_guess:
        print("Too high.")
    else:
        print("Too low.")