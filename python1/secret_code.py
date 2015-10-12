#!/usr/local/bin/python3
#
# Secret Code
# secret_code.py
#
# 2015 June 26th
#
""" Encodes an input line. """

# Tell the user to enter an input line
while True:
    input_line = input("Message: ").strip()
    if input_line:
        break
    print("Please enter one or more characters.")

# Save the next ordinal value of each character through a list comprehension
encoded_line = [chr(ord(character) + 1) for character in input_line]

# Print a reversed sequence of encoded_line
print("".join(reversed(encoded_line)))