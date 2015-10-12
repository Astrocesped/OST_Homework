#!/usr/local/bin/python3
#
# Text Transformer
# caser.py
#
# 2015 June 28th
#
""" Transforms string parameters according to specific input options. """

import sys

def exit(*args):
    """ Terminates the program. """
    print("Goodbye for now!")
    sys.exit()

# Dispatch table containing the possible functions to be selected
dispatch = {
    "capitalize": str.capitalize,
    "title": str.title,
    "upper": str.upper,
    "lower": str.lower,
    "exit": exit
    }
    
options = dispatch.keys()
    
while True:
    # Get the option that the user wishes to select
    function = input("Enter a function name({0}): ".format(", ".join(options))).strip()
    selection = dispatch.get(function, None)
    
    if selection:
        # Print the resulting text transformation (or quitting action)
        print(selection(input("Enter a string: ").strip()))
    else:
        print("Please enter a valid option.")