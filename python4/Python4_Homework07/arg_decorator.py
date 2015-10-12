#!/usr/local/bin/python3
#
# Python 4 Project 07 "Advance Use of Decorators" Homework
#
__author__ = "cmontesr"
'''
Created on Sep 14, 2015

arg_decorator.py: Provides a decorator function that adds an extra first
                  default argument to wrapped functions.
'''

from functools import wraps
from project_log import start_logging
from logging import info as log_info

start_logging()

def addarg(data):
    """
    Returns a decorator function that adds a default first positional
    argument to a wrapped function.
    :param data: Argument to be inserted on the wrapped function
    """
    
    def decorator(func):
        " Decorates the passed function. "
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            " Adds data to the function's signature. "
            log_info("Wrapping {0} with addarg".format(func.__name__))
            
            return func(data, *args, **kwargs)
        
        return wrapper
    
    log_info("addarg will decorate by adding the arg {0!r}".format(data))
    
    return decorator