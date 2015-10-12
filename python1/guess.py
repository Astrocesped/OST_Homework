#!/usr/local/bin/python3
#
# - Guess Game -
#  guess.py
#
# 2015 June 17th
#
""" Prompts the user to guess a number between 1 and 20. """

secret = 11
tries = 0
maximum_reached = False

while not maximum_reached:
    input_value = int(input("Guess a number: "))
    
    if input_value == secret:
        print("Correct! Well done, the number was", secret)
        break
    elif input_value > secret:
        print("Guess lower")
    else:
        print("Guess higher")
        
    tries += 1
    if tries == 5:
        maximum_reached = True
        
# If the while loop concluded normally, after reaching five guesses 
else:
    print("Sorry, the number was", secret)