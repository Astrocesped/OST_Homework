#!/usr/local/bin/python3
#
# Python 4 Project 06 "Using Exceptions Wisely" Homework
#
__author__ = "cmontesr"

'''
Created on Sep 13, 2015

exceptional_dict.py: Displays use of exceptions through a
                     special dict subclass.
'''

from project_log import start_logging
from logging import info as log_info
from logging import error as log_error

start_logging()

class ExceptionalDict(dict):
    def __init__(self, default):
        dict.__init__(self)
        self._default = default
        log_info("New ExceptionalDict instance created")
    
    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        
        except KeyError:
            log_error("Inexistent ExceptionalDict key given, return default")
            return self._default
        
        finally:
            log_info("ExceptionalDict's getitem successfully worked")
    
    # PROPERTIES (Protect the default value from being modified)
    @property
    def default(self):
        " Returns the default value of the instance. "
        return self._default
