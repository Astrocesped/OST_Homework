'''
Created on Aug 12, 2015

@author: cmontesr

Unittest module for find_regex.py
'''
import unittest
from find_regex import find_regular_expressions

class FindRegexTest(unittest.TestCase):

    def test_find_phrase(self):
        """
        Tests the find_regular_expressions function's returned value
        """
        
        self.assertEqual((231, 250), find_regular_expressions())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()