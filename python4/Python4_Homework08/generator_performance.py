#!/usr/local/bin/python3
#
# Python 4 Project 08 "Advanced Generators" Homework
#
__author__ = "cmontesr"

'''
Created on Sep 16, 2015

generator_performance.py: Provides examples of difference in performance
                          between generators and lists, by using the
                          timeit module's Timer class.
'''

from random import random

def million_random_list():
    " Returns a list with a million random numbers for the given range. "
    local_rand = random
    return [local_rand() for _ in range(1000000)]

def million_random_gen():
    " Generator function that returns a million random numbers. "
    local_rand = random
    for _ in range(1000000):
        yield local_rand()
        
def list_comprehension(collection):
    " Returns a list comprehension of a given collection. "
    return [i for i in collection]

def list_function(collection):
    " Applies the list() function to a given collection. "
    return list(collection)
