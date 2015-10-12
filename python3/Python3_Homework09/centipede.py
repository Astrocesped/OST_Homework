#!/usr/local/bin/python3
#
# Lesson 9: Special Object Methods Homework Project
#
'''
Created on Aug 20, 2015

@author: cmontesr

centipede.py: Practice for the use of special methods by implementing a
              'Centipede' class with several attributes and methods.
'''

class Centipede:
    """
    Class that implements several special methods, for learning purposes.
    """
    
    def __new__(cls):
        """
        Sets the initial variables of the class, before being instantiated
        """
        # Keeps a list of arguments passed to the instance, called as a method
        cls.stomach = []
        # Keeps a list of attribute names set to the instance
        cls.legs = []
        
        return object.__new__(cls)
        
    def __call__(self, arg):
        """
        Appends an argument to the stomach list upon the instance being called
        :param arg: Data to be added to stomach. No specific type required.
        """
        self.stomach.append(arg)
        
    def __repr__(self):
        " Represents the instance by printing the content of the legs list "
        return ",".join(self.legs)
        
    def __str__(self):
        " Returns a comma-delimited string of the stomach list "
        return ",".join(self.stomach)
    
    def __setattr__(self, key, value):
        " Sets a new attribute on the instance and adds its name to 'legs' "
        # Avoid the override of legs and stomach's value
        if key in ("stomach", "legs"):
            raise AttributeError("{0} is for internal use only".format(key))
        
        self.__dict__[key] = value
        self.legs.append(key)
