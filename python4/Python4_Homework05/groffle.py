#!/usr/local/bin/python3
#
# Lesson 05: "Optimizing Your Code" Homework
#

__author__ = "cmontesr"

'''
Created on Sep 12, 2015

groffle.py: Program for optimization. Python 4, Lesson 5. 

Calculates the groffle speed of a knurl widget 
of average density given by user input. 
'''

from math import log

def groffle_slow(mass, density):
    """
    Determines the... sum? of the natural logarithm of a certain
    volume, divided in 10000 consecutive segments.
    :param mass: Given mass to determine volume
    :param density: Given density to determine volume
    :return: Sum of each of the 10000 segments of the divided volume
    """
    total = 0.0 
    for i in range(10000): 
        masslog = log(mass * density) 
        total += masslog/(i+1)

    return total

def groffle_fast(mass, density):
    " Same purpose than groffle_slow. Aims to be faster."
    total = 0.0
    log_volume = log(mass * density)
    
    for i in range(1, 10001):
        total += log_volume / i
        
    return total

def groffle_faster(mass, density):
    """ Aims to be even faster than groffle_fast (less than a third of
    groffle_slow's original time)"""
    return log(mass * density) * sum((1 / i for i in range(1, 10001)))