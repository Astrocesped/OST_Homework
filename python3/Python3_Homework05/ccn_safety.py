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
    # Use capture groups to preserve the last four digits in the regex
    return re.sub(r"[\d]{4}-[\d]{4}-[\d]{4}-(?P<capture>[\d]{4})",
                  "XXXX-XXXX-XXXX-\g<capture>", text)