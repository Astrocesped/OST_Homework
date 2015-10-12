'''
Created on Sep 14, 2015

@author: cmontesr

Unittest for arg_decorator.py
'''
import unittest
from arg_decorator import *

class TestArgDecorator(unittest.TestCase):

    def test_extra_arg(self):
        
        @addarg("first")
        def testfunc(*args):
            " Simply returns a tuple with its arguments"
            return args
        
        self.assertEqual(testfunc("second", "third"),
                         ("first", "second", "third"))
        
        self.assertEqual(testfunc(2, 3), ("first", 2, 3))


if __name__ == "__main__":

    unittest.main()