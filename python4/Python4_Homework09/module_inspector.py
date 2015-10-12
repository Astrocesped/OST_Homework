#!/usr/local/bin/python3
#
# Lesson 09 "Uses of Introspection" Homework Project
#
__author__ = "cmontesr"
'''
Created on Sep 23, 2015

module_inspector.py: Provides inspection of a module's members.
'''
import inspect
from importlib import import_module
from project_log import start_logging
from logging import info as log_info
from logging import error as log_error

start_logging()

def def_inspect(module):
    """
    Scans a module's functions with inspect, returns their signatures, if any.
    :param module: Module, or name of module to be imported
    :return: String detailing the signature of each function in the module
    """
    # Take the __name__ attr of the module if the argument is not a string
    mod_name = module if isinstance(module, str) else module.__name__
    log_info("Attempting to inspect functions in module {}".format(mod_name))
    
    try:
        imported = import_module(str(mod_name))
        
    except ImportError as e:
        log_error(e)
        raise ImportError(e)
    
    result = []
    functions = inspect.getmembers(imported, inspect.isfunction)
    
    # For each function name, description tuple retrieved...
    for func, desc in functions:
        
        # ...Use getattr to take each function's signature
        func_txt = inspect.formatargspec(
                   *inspect.getfullargspec(getattr(imported, func)))
        
        result.append("'def {0}{1}'".format(func, func_txt))
    
    return "\n".join(result)