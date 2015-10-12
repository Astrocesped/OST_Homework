#!/usr/local/bin/python3
#
# First Tests with Functions
# three_params.py
#
# 2015 June 27th
#
""" Contains a function that can be called with a variable amount of arguments. """

def my_func(a, b="b was entered", c="c was not entered"):
    """ Prints the value of each one of its parameters. """
    
    print("{0}\n{1}\n{2}".format(a, b, c))

my_func("test")
my_func("test", b="test")
my_func("test", "test", "test")

print(my_func)