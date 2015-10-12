'''
Created on Aug 3, 2015

@author: cmontesr

Tests adder.py's functions.
'''
import unittest
import adder

class Test(unittest.TestCase):

    def test_successful_int_additions(self):
        """
        Test successful additions from add_two_integers.
        """
        self.assertEqual(adder.add_two_integers(3, 4), 7)
        self.assertEqual(adder.add_two_integers(10000000, 10000000),
                         20000000)
    
    def test_erroneous_int_additions(self):
        """
        Test wrong arguments passed to add_two_integers.
        """
        self.assertRaises(TypeError, lambda: adder.add_two_integers(9.6, 4))
        self.assertRaises(TypeError, lambda: adder.add_two_integers(9, "4"))
        self.assertRaises(TypeError, lambda: adder.add_two_integers(9j, self))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_successful_additions']
    unittest.main()