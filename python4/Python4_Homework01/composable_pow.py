#!/usr/local/bin/python3
#
# Lesson 01: "Further with Functions" Homework
#
__author__ = "cmontesr"

"""
2015 September 3rd

composable_pow.py: Extends the Composable class found in the
                    lesson's content.
"""
import types
from project_log import start_logging
from logging import info as log_info
from logging import error as log_error

class Composable:
    def __init__(self, f):
        """
        Stores a reference to a proxied function.
        :param f: Function namespace to be proxied
        """
        self.func = f
        start_logging()
        log_info("New Composable proxied function: {0}".format(f.__name__))
        
    def __call__(self, *args, **kwargs):
        """
        Proxy the function, passing all arguments through.
        """
        log_info("Proxied function called")
        return self.func(*args, **kwargs)
    
    def __mul__(self, other):
        """
        Return the composition of proxied and another function.
        :param other: Object to multiply the proxied with
        :return: Composition of the proxied function and the passed object
        """
        if type(other) is Composable:
            def anon(x):
                return self.func(other.func(x))
            
            log_info("{0} multiplied by Composable obj {1}".format(
                        self.func.__name__, other))
            return Composable(anon)
        
        elif type(other) is types.FunctionType:
            def anon(x):
                return self.func(other(x))
            
            log_info("{0} multiplied by function {1}".format(
                    self.func.__name__, other))
            return Composable(anon)
        
        log_error("Attempt to multiply {0} by {1}".format(
                    self.func.__name__, other))
        raise TypeError("Illegal operands for multiplication")
    
    def __pow__(self, other):
        """
        Returns the proxied function raised at an integer power.
        :param other: Object to raise the proxied with
        :return: Value of raised proxied function
        """
        if isinstance(other, int) and other >= 0:
            
            def anon_pow_times(*args):
                """
                Multiplies the proxied function as many times as
                the integer used to raise it.
                :param args: The args used for the original function
                :return: Proxied function multiplied as many times as other
                """
                # Return the proxied function at least once (in case other==0)
                result = self
                
                for _ in range(other-1):
                    result *= self

                return result(*args)
            
            log_info("{0} raised {1} times".format(self.func.__name__, other))
            return Composable(anon_pow_times)
        
        elif isinstance(other, int) and other < 0:
            log_error("Raised {0} w/ negative int".format(self.func.__name__))
            raise ValueError("Composable can only be raised w/ positive int")
        
        log_error("Attempt to raise {0} with type {1}".format(
                    self.func.__name__, type(other)))
        raise TypeError("Composable instance can only be raised w/ integers")
    
    def __repr__(self):
        return "<Composable function {0} at 0x{1:x}>".format(
                self.func.__name__, id(self))