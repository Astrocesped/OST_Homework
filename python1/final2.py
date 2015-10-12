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

def create_histogram(data_dict):
    """
    Creates a histogram according to the integer values
	contained inside a dict's values.
    :param data_dict: Dict containing integers as values; read as 'category': count
    :return: String to be printed by the caller.

    >>> print(len(create_histogram({1: 78, 4: 21, 8: 18, 10: 687, 14: 90, 16: 1000})))
    3471
    """
    histogram_str = []

    # Get the biggest count inside the data_dict's values
    biggest_quantity = 0
    for category in data_dict.keys():
        if data_dict[category] > biggest_quantity:
            biggest_quantity = data_dict[category]

    #  Round the Y axis line's highest value
	# to the second closest value in rounded hundreds
    biggest_yvalue = int(biggest_quantity/ 100) + 2

    # Get how many digits this biggest value has (plus the empty two
	# hundred above it) which will modify the whole table's horizontal
	# starting position by making a formatted string with such number of
	# places for the y axis.
    max_digits = "{{0:>{0}}} -|".format(len(str(biggest_quantity + 200)))

    def determine_stars(current_size):
        """
        Returns a list containing a set of strings according to the size of each dict value's count
        :return: List of string sets with either three asterisks or three spaces per value
        """

        asterisks = []

        for key in range(1, 17):
            key_value = data_dict.get(key, 0)

            if key_value >= current_size:
                asterisks.append("***")
            else:
                asterisks.append("   ")

        return asterisks

    for length in range(biggest_yvalue * 100, -20, -20):
        # If 0 has been reached, print a special X axis line; otherwise,
		# print asterisks and spaces, and current Y value if it ends with "00"

        if length == 0:
            histogram_str.append("".join([max_digits.format(0),
										 "-+-" * 16]).replace('|', '+'))
            break

        elif str(length).endswith("00"):
            histogram_str.append("".join([max_digits.format(length)] + determine_stars(length)))

        else:
            histogram_str.append("".join([max_digits.format(" ")] + determine_stars(length)))


    # X axis bottom line, containing 'categories' represented by integers, spread from 1 to 16
    histogram_str.append("".join([" " * len(str(biggest_quantity))] + ["  |"] + ["{0:^3}".format(i) for i in range(1, 17)]))

    return "\n".join(histogram_str)

def _test():
    """
    Test function.
    :return: Testmod console output.
    """
    import doctest, final2
    return doctest.testmod(final2)

# If there is an accompanying argument...
if len(sys.argv) >= 2:
    
    try:
        # Open the file and proceed to execute both functions from above
        with open(os.path.normpath(sys.argv[1]), "r") as f:
            word_count = word_grouper(f.read().strip())
            print(dict_to_str(word_count, ["Word Length", "Count"]))

            print()

            print(create_histogram(word_count))
            
    except FileNotFoundError:
        print("Couldn't find the specified file. Quitting.")
    except IsADirectoryError:
        print("The specified argument is a directory. Quitting.")

elif __name__ == "__main__":
    _test()
