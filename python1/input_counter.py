#!/usr/local/bin/python3
#
# input_corner.py
#
# 2015 June 20th
#
''' Displays the order in which words in a sentence were first
written through standard input. '''

import string

# Empty set and dict. Former saves unique words in the input,
# latter saves the order in which they were first found through all input.
unique_set = set()
counter_dict = {}
set_size = 0 # Counter for the current number of words in the set

while True:
    input_line = input("Enter text: ").strip().lower()
    # Finish if input is empty
    if not input_line:
        break
        
    # Get rid of punctuation characters
    for punc in string.punctuation:
        input_line = input_line.replace(punc, "")
        
    # Enter each word into the set
    for word in input_line.split():            
        unique_set.add(word)
        
        if len(unique_set) > set_size:
            set_size += 1
            counter_dict[word] = set_size
            
    #Print each word's first ocurrence so far
    for key in sorted(counter_dict.keys()):
        print(key, counter_dict[key])
    
print("Finished")