#!/usr/local/bin/python3
#
# Word Length Reader
# final.py
#
# 2015 July 1st
#
""" Reads a file passed as argument and displays
the count of each word length found inside. """

import os
import sys
import string

def word_grouper(text):
    """
    Counts all unique word lengths inside a string.
    :param text: String to be analyzed
    :return: Dict containing 'word length': 'count' pair of values

    >>> test = word_grouper("-Do you sometimes miss Ace of Base? -Always.")
    >>> for key in sorted(test.keys()):
    ...     print(key, test[key])
    2 2
    3 2
    4 2
    6 1
    9 1
    """
    length_dict = {}

    # Remove all punctuation from the string
    for mark in string.punctuation:
        text = text.replace(mark, "")

    # Enter each word's length into the dict
    for word in text.strip().split():
        length_dict[len(word)] = length_dict.get(len(word), 0) + 1

    return length_dict


def dict_to_str(data_dict, column_names):
    """
    Prints a dictionary in an easy to read format.
    :param data_dict: Dict containing the elements to be printed.
    :param column_names: List containing the name of each column.
    :return: Formatted string

    >>> print(dict_to_str({1: 'test', 100: 'hey', 40: 90}, ['Key', 'Value']))
    ----- Key ------ ---- Value -----
                   1             test
                  40               90
                 100              hey
    """
    formatted_dict = []
    header = []

    # Make the header lines
    for name in column_names:
        header.append("{0:-^16}".format(" " + name + " "))

    formatted_dict.append(" ".join(header))

    # Attach the data_dict in string form
    for key in sorted(data_dict.keys()):
        formatted_dict.append("{0:>16} {1:>16}".format(key, data_dict[key]))

    return "\n".join(formatted_dict)

def _test():
    """
    Test function.
    :return: Testmod console output.
    """
    import doctest, final
    return doctest.testmod(final)

# If there is an accompanying argument...
if len(sys.argv) >= 2:
    
    try:
        # Open the file and proceed to execute both functions
        with open(os.path.normpath(sys.argv[1]), "r") as f:
            print(dict_to_str(word_grouper(f.read().strip()), ["Word Length", "Count"]))
            
    except FileNotFoundError:
        print("Couldn't find the specified file. Quitting.")
    except IsADirectoryError:
        print("The specified argument is a directory. Quitting.")

elif __name__ == "__main__":
    _test()
