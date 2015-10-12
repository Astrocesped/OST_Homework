#!/usr/local/bin/python3
#
# Lesson 13 "Functions and Other Objects" Homework Project
#
__author__ = "cmontesr"
'''
Created on Sep 27, 2015

sstr.py: Provides an str subclass that allows cyclic shifting of
         its characters.
'''

class sstr(str):
    
    def __lshift__(self, shift):
        """
        Shifts the instance's characters from right to left for as many
        characters as pointed.
        :param shift: Integer detailing how many spaces to shift
        :return: An sstr instance with the same value as this instance
        """
        if not isinstance(shift, int):
            raise TypeError("sstr's << operator only compatible w/ integers")
        
        # The shifting spaces will be equal to the module operation of
        # shift against the instance's length
        spaces = (shift % len(self))

        self = self[spaces:] + self[:spaces]
        return sstr(self)
    
    def __rshift__(self, shift):
        """
        Shifts the instance's characters from left to right for as many
        characters as pointed.
        :param shift: Integer detailing how many spaces to shift
        :return: An sstr instance with the same value as this instance
        """
        if not isinstance(shift, int):
            raise TypeError("sstr's >> operator only compatible w/ integers")
        
        # The shifting spaces will be equal to the module operation of
        # shift against the instance's length (negative in this case)
        spaces = -(shift % len(self))

        self = self[spaces:] + self[:spaces]
        return sstr(self)
