'''
Created on Sep 16, 2015

@author: cmontesr
'''
import unittest
from timeit import Timer
from generator_performance import *

class TestGenPerformance(unittest.TestCase):
    
    def setUp(self):
        self.lc1 = Timer("t1 = list_comprehension(million_random_list())",
                         "from __main__ import list_comprehension, million_random_list")
        
        self.lc2 = Timer("t2 = list_comprehension(million_random_gen())",
                         "from __main__ import list_comprehension, million_random_gen")
        
        self.lf1 = Timer("t3 = list_function(million_random_list())",
                         "from __main__ import list_function, million_random_list")
        
        self.lf2 = Timer("t4 = list_function(million_random_gen())",
                       "from __main__ import list_function, million_random_gen")

    def test_list_comprehensions(self): 
        """ Tests the difference between using a generator and a list,
        after applying a list comprehension to their output. """
        self.assertAlmostEqual(self.lc2.timeit(number=1),
                             self.lc1.timeit(number=1), 1)
        
    def test_list_functions(self):
        """ Tests the difference between using a generator and a list,
        after applying list() to their output. """
        self.assertLessEqual(self.lf1.timeit(number=1),
                             self.lf2.timeit(number=1))
        
    def test_generators(self):
        """ Tests difference between using a list comprehension and list()
        on the generators. """
        self.assertLessEqual(self.lf1.timeit(number=1),
                             self.lc1.timeit(number=1))
        
    def test_lists(self):
        """ Tests difference between using a list comprehension and list()
        on the lists. """
        self.assertLessEqual(self.lf2.timeit(number=1),
                             self.lc2.timeit(number=1))


if __name__ == "__main__":

    unittest.main()