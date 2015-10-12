#!/usr/local/bin/python3
#
# Lesson 02: "Data Structures" Homework
#
__author__ = "cmontesr"

'''
Created on Sep 5, 2015

@author: cmontesr

arr_3d.py: Extends the two-dimensional list from Lesson 02 to
           have it save a three-dimensional structure.
'''
from array import array as sys_array
from project_log import start_logging
from logging import info as log_info

start_logging()

def array_func(x, y, z):
    """
    Creates a list of lists of lists.
    :param x: Integer size of the first level of the array
    :param y: Size of the second level
    :param z: Size of the third level
    :return: Three-dimensional list, filled with 0s
    """
    rows = []
    
    for _ in range(x):
        d3_rows = []
        for _ in range(y):
            d3_rows.append([0] * z)
        rows.append(d3_rows)
    
    log_info("Array created by array_func: {0}".format(rows))
    
    return rows

class Array:
    def __init__(self, X, Y, Z):
        """
        Create an X-element list of Y-element lists of Z-element lists.
        """
        self._x = X
        self._y = Y
        self._z = Z
        self.array_len = 0
        
    def _validate_key(self, key):
        """
        Validate a key against the array's shape, returning good tuples.
        Raises KeyError on problems.
        """
        x, y, z = key
        
        if (0 <= x < self._x and 0 <= y < self._y and  0 <= z < self._z):
            return key
        
        raise KeyError("Subscript out of range")
        

class List_of_lists_array(Array):
    """
    Allows use of list of lists of lists through "tuple of
    subscripts" notation
    """
    
    def __init__(self, x, y, z):
        " Create lists of lists of lists in the same way than array_func. "
        Array.__init__(self, x, y, z)
        self._data = []
    
        for _ in range(x):
            d3_rows = []
            for _ in range(y):
                d3_rows.append([0] * z)
                self.array_len += 1
            
            self._data.append(d3_rows)
            
        log_info("New List_of_lists_array instance. Dimensions: {0}".format(
                [x, y, z]))
    
    def __delitem__(self, key):
        """
        Deletes the appropriate element from _data whtough subscripting.
        """
        x, y, z = self._validate_key(key)
        
        log_info("Deleting: {0} from List_of_lists_array ins in {1}".format(
                self._data[x][y][z], [x, y, z]))
        del self._data[x][y][z]
        self.array_len -= 1
            
    def __getitem__(self, key):
        """
        Returns the appropriate element for a three-element subscript tuple.
        """
        x, y, z = self._validate_key(key)
        return self._data[x][y][z]

    def __setitem__(self, key, value):
        """
        Sets the appropriate element for a three-element subscript tuple.
        """
        x, y, z = self._validate_key(key)
        self._data[x][y][z] = value
        log_info("Set value: {0} for List_of_lists_array element {1}".format(
                value, [x, y, z]))


class Single_list_array(Array):
    def __init__(self, x, y, z):
        Array.__init__(self, x, y, z)
        self._data = [0] * x * y * z
        
        log_info("New Single_list_array instance. Content: {0}".format(
                self._data))
    
    def __delitem__(self, key):
        x, y, z = self._validate_key(key)
        pos = (x * self._x * 2) + (y * self._y) + z
        
        self._log_array_info(self._data[pos], pos, "Deleting")
        del self._data[pos]
        self.array_len -= 1
      
    def __getitem__(self, key):
        x, y, z = self._validate_key(key)
        return self._data[(x * self._x * 2) + (y * self._y) + z]
    
    def __setitem__(self, key, value):
        x, y, z = self._validate_key(key)
        pos = (x * self._x * 2) + (y * self._y) + z
        
        self._data[pos] = value
        self._log_array_info(value, pos, "Setting")
    
    def _log_array_info(self, new_value, position, action):
        log_info("{0} value {1} in Single_list_array ins[{2}]: {3}".format(
                action, new_value, position, self._data))
        

class Array_module_array(Single_list_array):
    """
    Creates a single list array with the help of the 'array' module.
    """
    def __init__(self, x, y, z):
        Array.__init__(self, x, y, z)
        self._data = sys_array("i", [0] * x * y * z)
        
        log_info("New Array_module_array instance. Content: {0}".format(
                self._data))
    
    def _log_array_info(self, new_value, position, action):
        log_info("{0} value {1} in Array_module_array ins[{2}]: {3}".format(
                action, new_value, position, self._data))
        
    
class Dict_array(Array):
    def __init__(self, x, y, z):
        Array.__init__(self, x, y, z)
        self._data = {}
        
        log_info("New Dict_array instance created.")
        
    def __delitem__(self, key):
        x, y, z = self._validate_key(key)
        
        log_info("Deleting value {0} in Dict_array ins key {1}".format(
                self._data[x, y, z], key))
        
        del self._data[x, y, z]
        self.array_len -= 1
    
    def __getitem__(self, key):
        x, y, z = self._validate_key(key)
        return self._data.get((x, y, z), 0)
    
    def __setitem__(self, key, value):
        x, y, z = self._validate_key(key)
        self._data[x, y, z] = value
        
        log_info("Set value {0} in Dict_array ins key {1}".format(value, key))