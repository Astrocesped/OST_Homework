#!/usr/local/bin/python3
#
# Adder
# adder.py
#
"""
Contains functions related to adding elements
"""

def add_two_integers(num1, num2):
    """
    Takes two integers and returns their sum. Raises TypeError if
    any of them are not integer types.
    :param num1: Integer 1
    :param num2: Integer 2
    :return: Integer, result of the sum of both integers above
    """
    if type(num1) == int and type(num2) == int:
        return num1 + num2
    
    raise TypeError("Both arguments should be of the integer type")
    