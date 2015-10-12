#!/usr/local/bin/python3
#
# Input Saver
# inputter.py
#
# First draft: 2015 June 22nd
# Second draft: 2015 June 24th
#
""" Reads input lines and saves them to a text file. """

filename = "input_saver.txt"

# Create the file, if it doesn't exist
saver = open(filename, "a")
saver.close()

# Display current content of the file
print("Current contents of 'input_saver.txt':\n")
display  = open(filename, "r")
print(display.read())
display.close()
print("\n", "*" * 15, "\n")

while True:
    # Take user input until nothin is entered
    input_string = input("Enter text: ").strip()

    if not input_string:
        break
        
    # Write into the file the input string
    f = open(filename, "a")
    f.write(input_string)
    f.close()
    
    # Print to the console the current content of the file
    f = open(filename, "r")
    print(f.read())
    f.close()
    
print("Finished.")
