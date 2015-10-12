#!/usr/local/bin/python3
#
# Lesson 12: Input Engineering Homework Project
#
'''
Created on Aug 24, 2015

@author: cmontesr

property_address.py: Address verification through classes, special
                    methods and properties. Also used as a practice
                    for line-command parsing and configuration file use.
'''

import logging
from os import path
from re import compile
from configparser import RawConfigParser

# Logging global variables
CFG_FILENAME = path.join("src", "property_address.cfg")
LOG_FILENAME = path.join("src", "property_address.log")
LOG_FORMAT = ("%(asctime)s - %(levelname)s - %(funcName)s - %(message)s")
DEFAULT_LOG_LEVEL = "INFO"
LEVELS = {
          "DEBUG": logging.DEBUG,
          "INFO": logging.INFO,
          "WARNING": logging.WARNING,
          "ERROR": logging.ERROR,
          "CRITICAL": logging.CRITICAL
          }

# Pre-compiled regular expressions to help look for address patterns
STATE_REGEX = compile("^[A-Z]{2}$")
ZIP_REGEX = compile("^[0-9]{5}$")

class Address:
    """ Keeps an user's US address with verified properties. """
    def __init__(self, name, street_address, city, state, zip_code):
        self._name = name
        self.street_address = street_address
        self.city = city
        
        #Validate and set state and zip code
        self.validate_state(state)
        self.validate_zip_code(zip_code)
        
        logging.info("Created new Address with name {0}".format(self._name))
        
    ######### PROPERTY HANDLERS #########
    
    @property
    def name(self):
        " Retrieves the user's name. "
        return self._name
    
    @name.setter
    def name(self, value):
        " Protects the user's name from being modified. "
        msg = "NameException raised: Name attribute is immutable"
        logging.error(msg)
        raise NameException(msg)
    
    @property
    def state(self):
        " Retrieves the address' state. "
        return self._state
    
    @state.setter
    def state(self, value):
        """
        Calls validate_state to determine whether to set _state or not.
        :param value: State name to be evaluated through validate_state
        """
        self.validate_state(value)
        logging.info("New state name set: {0}".format(value))
        
    @property
    def zip_code(self):
        " Retrieves the address' zip code. "
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, value):
        """
        Calls validate_zip_code to determine whether to set _zip_code or not.
        :param value: Zip code to be evaluated through validate_zip_code
        """
        self.validate_zip_code(value)
        logging.info("New zip_code set: {0}".format(value))
    
    ######### HELPER FUNCTIONS #########
    
    def validate_state(self, state):
        """
        Checks for a state name to only contain two capital letters.
        Sets the new _state or raises a StateError otherwise.
        :param state: State name to be evaluated through STATE_REGEX
        """
        if STATE_REGEX.match(state):
            self._state = state
        else:
            msg = "StateError raised: Erroneous state name attempted"
            logging.error(msg)
            raise StateError(msg)
        
    def validate_zip_code(self, zip_code):
        """
        Checks for a zip code to only contain five consecutive digits.
        Sets the new _zip_code or raises a ZipCodeError otherwise.
        :param value: Zip code to be evaluated through ZIP_REGEX
        """
        if ZIP_REGEX.match(zip_code):
            self._zip_code = zip_code
        else:
            msg = "ZipCodeError raised: Erroneous zip code attempted"
            logging.error(msg)
            raise ZipCodeError(msg)
    
    ######### MAGIC METHODS #########
    
    def __str__(self):
        text = ["Address object named {0} with address: ".format(self._name),
                ", ".join([self.street_address, self.city,
                           self._state, self._zip_code])]
        return "".join(text)
        
class NameException(Exception):
    """ Custom Exception to be raised in case there's an attempt to modify
    an Address instance's name. """
    pass

class StateError(Exception):
    " Custom error to be raised in case there's an erroneous state name. "
    pass


class ZipCodeError(Exception):
    " Custom error to be raised in case there's an erroneous zip code. "
    pass


########## HELPER FUNCTIONS ##########

def read_config_file(filename):
    """
    Reads a configuration file to modify the global settings.
    :param filename: cfg file pathname, read through os.path.normpath
    """
    global LOG_FORMAT, LOG_FILENAME, STATE_REGEX, ZIP_REGEX
    
    # Config parser object, load settings for global variables
    config = RawConfigParser()
    config.read(path.normpath(filename))

    # Sections should be "log" and "validators"
    for section in config.sections():
        # Options for log: format, output
        # Options for validators: zip_code, state
        for option in config.options(section):

            if section == "log" and option == "format":
                LOG_FORMAT = config.get(section, option)
            elif section == "log" and option == "output":
                LOG_FILENAME = config.get(section, option)
            elif section == "validators" and option == "state":
                STATE_REGEX = compile(config.get(section, option))
            elif section == "validators" and option == "zip_code":
                ZIP_REGEX = compile(config.get(section, option))

def start_logging(filename=LOG_FILENAME, log_level=DEFAULT_LOG_LEVEL):
    """
    Starts logging to the given filename and logging level.
    :param filename: Filepath to be read through os.path.normpath
    :param log_level: Log level to be set
    """
    logging.basicConfig(filename=path.normpath(filename),
                        level=LEVELS[log_level], format=LOG_FORMAT)
    logging.info("New logging session for property_address.py")

if __name__ == "__main__":
    from optparse import OptionParser
    
    # Create a parser for command-line options
    parser = OptionParser()
    # Read the configuration file
    read_config_file(CFG_FILENAME)
    # Help string for the options with similar statements
    help_str = "Sets the {0} value of the Address object"
    
    parser.add_option("-l", "--loglevel", action="store", dest="level",
                      default="INFO", help= ("Sets the log level to: "
                                             "{0}".format(",".join(LEVELS))))
    parser.add_option("-n", "--name", dest="name", action="store",
                      help=help_str.format("name"))
    parser.add_option("-a", "--address", dest="st_address", action="store",
                      help=help_str.format("street_address"))
    parser.add_option("-c", "--city", dest="city", action="store",
                      help=help_str.format("city"))
    parser.add_option("-s", "--state", dest="state", action="store",
                      help=help_str.format("state"))
    parser.add_option("-z", "--zip", dest="zip_code", action="store",
                      help=help_str.format("zip_code"))
    
    # If any of the options without a default is empty, throw parser error
    # describing the short name of each missing option
    options, args = parser.parse_args()
    missing = [("-" + str(o)[0]) for o in options.__dict__.keys()
               if not options.__dict__[o]]
    if len(missing) == 5:
        # If all non-default options are empty, display them in specific order
        parser.error("options -n, -a, -c, -s, -z are required")
    elif missing:
        # Else display the particularly missing ones
        parser.error("options {0} are required".format(", ".join(missing)))
        
    # Start logging
    start_logging(log_level=str.upper(options.level))
    
    # Try to create Address, catch custom errors otherwise
    try:
        print("Created {0}".format(str(
              Address(options.name, options.st_address, options.city,
                      options.state, options.zip_code))))
        
    except StateError:
        parser.error(("option -s must follow the regex: "
                      "{0}".format(STATE_REGEX.pattern)))
        
    except ZipCodeError:
        parser.error(("option -z must follow the regex: "
                      "{0}".format(ZIP_REGEX.pattern)))
