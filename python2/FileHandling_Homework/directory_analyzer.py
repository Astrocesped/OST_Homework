#!/usr/local/bin/python3
#
# Directory Content Analyzer
# directory_analyzer.py
#
# 2015 July 5th
#
""" Analyzes the files contained in the current working directory and prints a report. """

import glob
import os

def extension_count_dict():
    """ Gets the current files' extension in the directory and counts them.
    :return: Dict containing each extension as key, and its count as value.
    """
    ext_counter = {}
    files = glob.glob("*")
    
    # Fill the dict with each file's extension count
    for fn in files:
        # If the element is not a file, keep iterating
        if not os.path.isfile(fn):
            continue
        
        f_ext = os.path.splitext(fn)[1]
        # Remove the period from the file extension
        ext_counter[f_ext[1:]] = ext_counter.get(f_ext[1:], 0) + 1
        
    return ext_counter

def dict_to_str(data_dict, column_names):
    """
    Transforms a passed dict's content to an easy to read list format.
    :param data_dict: Dict containing the elements to be printed.
    :param column_names: List containing the name of each column.
    :return: Formatted string
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

if __name__ == "__main__":
    print(dict_to_str(extension_count_dict(), ["Extension", "Count"]))