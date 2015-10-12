#!/usr/local/bin/python3
#
# Lesson 10: Properties Homework Project
#
'''
Created on Aug 22, 2015

@author: cmontesr

property_address.py: Address verification through classes, special
                    methods and properties.
'''

import re

# Pre-compiled regular expressions to help look for address patterns
state_regex = re.compile("^[A-Z]{2}$")
zip_regex = re.compile("^[0-9]{5}$")

class Address:
    """ Keeps an user's US address with verified properties. """
    def __init__(self, name, street_address, city, state, zip_code):
        self._name = name
        self.street_address = street_address
        self.city = city
        self._state = state
        self._zip_code = zip_code
        
    ######### PROPERTY HANDLERS #########
    
    @property
    def name(self):
        " Retrieves the user's name. "
        return self._name
    
    # Not implementing a setter after defining a getter raises AttributeError
    
    @property
    def state(self):
        " Retrieves the address' state. "
        return self._state
    
    @state.setter
    def state(self, value):
        """
        Checks for a state name to only contain two capital letters.
        Sets the new _state or raises a StateError otherwise.
        :param value: State name to be evaluated through state_regex
        """
        if state_regex.match(value):
            self._state = value
        else:
            raise StateError("Erroneous state name entered")
        
    @property
    def zip_code(self):
        " Retrieves the address' zip code. "
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, value):
        """
        Checks for a zip code to only contain five consecutive digits.
        Sets the new _zip_code or raises a ZipCodeError otherwise.
        :param value: Zip code to be evaluated through zip_regex
        """
        if zip_regex.match(value):
            self._zip_code = value
        else:
            raise ZipCodeError("Erroneous zip code entered")
        

class StateError(Exception):
    " Custom error to be raised in case there's an erroneous state name. "
    pass


class ZipCodeError(Exception):
    " Custom error to be raised in case there's an erroneous zip code. "
    pass