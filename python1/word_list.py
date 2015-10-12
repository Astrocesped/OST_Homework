#!/usr/local/bin/python3
#
# Lower and uppercase word counter
# world_list.py
#
# 2015 June 18th
#
""" Reads a string from input and print a list of its words with an upper-case letter in them
and then the rest of its words. """

import string

words = input("Input your text: ").strip().split()

uppercase_words = [] # Array that will hold words with at least one upper letter
other_words = [] # Array that will hold the rest of the words

# Tell user to type at least one set of characters if words is empty
# if so, nothing else will happen
if not words:
    print("Please type at least one word or set of characters.")

for word in words:
    # Check each letter of every word for uppercase
    for letter in word:
        if letter in string.ascii_uppercase:
            uppercase_words.append(word)
            break
    # If previous for loop ends normally, word has no uppercase letters
    else:
        other_words.append(word)

index_counter = 0 # Counter for the single for loop, so that there are no index errors on both lists

# Print uppercase_words first, and other_words afterwards
for i, word in enumerate(words):
    # Print uppercase_words if enumeration is smaller than that list's length
    if i < len(uppercase_words):
        print(uppercase_words[index_counter])
        index_counter += 1
    # If the first list is finished, reset the index_counter and print the first 'other' word
    elif i == len(uppercase_words):
        print(other_words[0])
        index_counter = 1
    # Print the rest of the words
    else:
        print(other_words[index_counter])
        index_counter += 1