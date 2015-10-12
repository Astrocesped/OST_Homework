#!/usr/local/bin/python3
#
# 2015 August 12
# Lesson 4: Regular Expressions Homework Project
#
"""
find_regex.py: Finds the start and end positions of phrases
               through Regular Expressions.
"""

import re

def find_regular_expressions():
    """
    Searches for the occurrence of the phrase "Regular Expressions" inside
    a pre-determined string.
    :return: Tuple containing the start and end position of the occurrence of
             the aforementioned phrase inside the string
    """
    
    text = """\
In the 1950s, mathematician Stephen Cole Kleene described automata theory \
and formal language theory in a set of models using a notation called \
"regular sets" as a method to do pattern matching. Active usage of this \
system, called Regular Expressions, started in the 1960s and continued under \
such pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, Ken \
Thompson, and Henry Spencer."""
    
    match = re.search("Regular Expressions", text)
    
    return match.span()
    