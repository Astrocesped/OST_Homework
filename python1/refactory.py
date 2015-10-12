#!/usr/local/bin/python3
#
# Refactoring a Function
# refactory.py
#
# 2015 July 1st
#
""" Reinforces the concept of refactoring. """

small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')

def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.
    
    title: String to be formatted

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """
    
    lst_of_words = title.lower().split()
    new_title = []
    
    for i, word in enumerate(lst_of_words):
        # Append the word as is if it's in the global list and not the first one; otherwise, capitalize it
        new_title.append(word if word in small_words and i != 0 else str.capitalize(word))
            
    return " ".join(new_title)

def _test():
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()