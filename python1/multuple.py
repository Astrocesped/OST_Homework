#!/usr/local/bin/python3
#
# Multiplying table
# multuple.py
#
# 2015 June 21
#
""" Prints a multiplying table of formatted strings
from a tuple of number pairs. """

# Main tuple that will hold the two-element tuples
tuples = ((1, 1), (2, 2), (12, 13), (4, 4), (99, 98))

for x, y in tuples:
    # Print a formatted string of the product of each multiplication
    print("{0:>4d} = {1:>2d} x {2:>2d}".format(x * y, x, y))