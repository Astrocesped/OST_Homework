#!/usr/local/bin/python3
#
# Lesson 14 "Context Managers"
#
__author__ = "cmontesr"
'''
Created on Sep 28, 2015

cm_exceptions.py: Provides context manager classes that don't allow a certain
                  type of exception to be raised inside its suite.
'''
from project_log import start_logging, log_info

start_logging()

class CM_AvoidExceptions:
    """
    Context Manager class that avoids a list of Exceptions to be raised
    inside the indented suite.
    """
    
    def __init__(self, *exceptions):
        " Receives Exception classes that will be allowed to be raised. "
        self.exceptions = list(exceptions)
        log_info("New CM_AvoidExceptions against {}".format(self.exceptions))
    
    def __enter__(self):
        pass
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        log_info("A {} has been detected".format(exc_type))
        
        # Run through the exception list received
        for self_exc in self.exceptions:
            if isinstance(exc_type, self_exc):
                log_info("Avoiding {} to be raised".format(exc_type))
                return False
            
        return True