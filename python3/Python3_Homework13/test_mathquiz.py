'''
Created on Aug 30, 2015

@author: cmontesr

Unittest module for mathquiz.py
'''

import unittest
from math import fsum
from mathquiz import *

class Test_MathQuiz(unittest.TestCase):

    def setUp(self):
        self.sum_array = [t for t in int_pair_generator()]
        
    def test_right_guesses(self):
        for i, t in enumerate(range(len(self.sum_array))):
            self.assertTrue(verify_sum(self.sum_array[i], 
                                       sum(self.sum_array[i])))
        
    def test_wrong_guesses(self):
        for i, t in enumerate(range(len(self.sum_array))):
            self.assertFalse(verify_sum(self.sum_array[i],
                                        sum(self.sum_array[i]) - 2))
            
    def test_time_results(self):
        times = (3, 4, 5, 6, 7)
        t_results = time_results(times)
        
        # Total time
        self.assertEqual(fsum(times), t_results[0])
        # Time averages
        self.assertEqual(fsum(times) / len(times), t_results[1])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()