#!/usr/local/bin/python3
#
# Lesson 11: Logging Introduction Homework Project
#
'''
Created on Aug 23, 2015

@author: cmontesr

property_address.py: Address verification through classes, special
                    methods and properties. It also provides a first
                    look into logging.
'''

import re
import logging

# Logging global variables
LOG_FILENAME = "property_address.log"
LOG_FORMAT = ("%(asctime)s - %(levelname)s - %(funcName)s - %(message)s")
DEFAULT_LOG_LEVEL = "info"
LEVELS = {
          "debug": logging.DEBUG,
          "info": logging.INFO,
          "warning": logging.WARNING,
          "error": logging.ERROR,
          "critical": logging.CRITICAL
          }

def start_logging(filename=LOG_FILENAME, log_level=DEFAULT_LOG_LEVEL):
    """
    Starts logging to the given filename and logging level
    """
    logging.basicConfig(filename=filename, level=LEVELS[log_level],
                        format=LOG_FORMAT)
    logging.info("New logging session for property_address.py")

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
        
        logging.info("Creating a new address")
        
    ######### PROPERTY HANDLERS #########
    
    @property
    def name(self):
        " Retrieves the user's name. "
        return self._name
    
    @name.setter
    def name(self, value):
        " Protects the user's name from being modified. "
        msg = "Name attribute is immutable"
        logging.error(msg)
        raise AttributeError(msg)
    
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
            logging.info("New state name set")
        else:
            msg = "StateError: Erroneous state name attempted"
            logging.error(msg)
            raise StateError(msg)
        
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
            logging.info("New zip code set")
        else:
            msg = "ZipCodeError: Erroneous zip code attempted"
            logging.error(msg)
            raise ZipCodeError(msg)
        

class StateError(Exception):
    " Custom error to be raised in case there's an erroneous state name. "
    pass


class ZipCodeError(Exception):
    " Custom error to be raised in case there's an erroneous zip code. "
    pass