'''
Created on Sep 3, 2015

@author: cmontesr

composable_pow.py: Unittest module for composable_pow.py
'''
import unittest
from composable_pow import *

def double_it(x):
    " Returns a number doubled. "
    return x*2

class TestComposablePow(unittest.TestCase):

    def setUp(self):
        self.power = Composable(double_it)

    def test_composable_pow(self):
        once = self.power ** 0
        twice = self.power ** 2
        thrice = self.power ** 3
        fiveice = self.power ** 5
        
        self.assertEqual(once(2), 4)
        self.assertEqual(twice(2), 8)
        self.assertEqual(thrice(2), 16)
        self.assertEqual(fiveice(2), 64)
        
    def test_wrong_pow(self):
        with self.assertRaises(TypeError):
            nonint = self.power ** "two"
            
        with self.assertRaises(ValueError):
            negint = self.power ** -4


if __name__ == "__main__":
    
    unittest.main()