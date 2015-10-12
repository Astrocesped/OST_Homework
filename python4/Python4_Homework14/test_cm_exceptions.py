'''
Created on Sep 28, 2015

@author: cmontesr

Unittest for cm_exceptions.py
'''
import unittest
from cm_exceptions import *

class Test(unittest.TestCase):

    def test_exercise(self):
        with CM_AvoidExceptions(ValueError):
            e0 = int("no")
            
            self.assertRaises(ZeroDivisionError, 3 / 0)
            self.assertRaises(NameError, non_existant[2])
            
            arr = []
            self.assertRaises(IndexError, arr[2])
            
    def test_custom(self):
        with CM_AvoidExceptions(Exception) as e:
            e0 = int("no")
            e1 = 3 / 0
            
    def test_many(self):
        with CM_AvoidExceptions(ArithmeticError, NameError):
            e0 = 3 / 0
            e1 = non_existant[2]

            self.assertRaises(ValueError, int("no"))
        

if __name__ == "__main__":

    unittest.main()