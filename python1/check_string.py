#!/usr/local/bin/python3
# check_string.py
#
""" Checks if an input string is upper case and ends with a period.
Notifies if either, neither or both of these clauses are met. """

input_str = input("Enter an uppercase string ending with a period: ")

period = input_str.endswith('.')
up = input_str.isupper()

if period and up:
    print("Input meets both requirements.")
else:
    if not period:
        print("Input does not end with a period.")
    if not up:
        print("Input is not all upper case.")