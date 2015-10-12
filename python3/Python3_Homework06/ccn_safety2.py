#!/usr/local/bin/python3
#
# 2015 August 14
# Lesson 5: More On Regular Expressions Homework Project
#
"""
ccn_safety.py: Contains functions related to the safe display of credit
               card properties.
"""

import re

def substitute_ccn(text):
    """
    Replaces all of the digits in a standard credit card number for an 'X'
    character, except for the last four, though Regular Expressions
    :param text: String to be formatted
    :return: Converted string
    """
    # Create a pattern object
    pattern = re.compile(r"""
        [\d]{4}     # The first four digits of a credit card number
        -[\d]{4}    # The second set of four digits of a CCN, with '-' prefix
        -[\d]{4}    # The third set of four digits of a CCN, with '-' prefix
        -[\d]{4}    # The last set of four digits of a CCN, with '-' prefix
        """, re.VERBOSE)
    
    return pattern.sub("CCN REMOVED FOR YOUR SAFETY", text)