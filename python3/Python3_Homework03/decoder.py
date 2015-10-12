#!/usr/local/bin/python3

"""
decoder.py: Contains classes that transform certain values into
            their equivalent, under a certain context.
"""

class alphabator:
    """
    Iterator that converts integers from 1 to 26 into their corresponding
    ordinal Unicode character value. Other objects return as-is.
    """
    
    def decode_item(self, item):
        if isinstance(item, int) and item < 27 and item > 0:
            return chr(item + 64)
        
        return item
    
    def __init__(self, lst):
        """
        Initialize the iterator object.
        :param lst: List or tuple of objects.
        """
        self.array = lst
        
        # Variable used for iteration
        self.item_no = 0
    
    def __iter__(self):
        " Allow instance to be iterated over. "
        return self
    
    def __next__(self):
        """
        Return the next value in the sequence. Pass each item
        through the decode_item method.
        """
        
        try:
            val = self.decode_item(self.array[self.item_no])
        except IndexError:
            raise StopIteration
        
        self.item_no += 1
        return val
