'''
Created on Sep 27, 2015

@author: cmontesr

Unittest module for sstr.py
'''
import unittest
from sstr import *

class TestSstr(unittest.TestCase):

    def test_sstr_exercise(self):
        s1 = sstr("abcde")

        self.assertEqual('abcde', s1 << 0)
        self.assertEqual('abcde', s1 >> 0)
        self.assertEqual('cdeab', s1 << 2)
        self.assertEqual('deabc', s1 >> 2)
        self.assertEqual('abcde', s1 >> 5)
        
        self.assertTrue((s1 >> 5) << 5 == 'abcde')
        
    def test_sstr_extra(self):
        s2 = sstr(12345)
        
        self.assertEqual('12345', s2 << 10)
        self.assertEqual('45123', s2 >> 12)
        self.assertEqual('51234', s2 << 14)
        self.assertEqual('34512', s2 >> -7)
        
        with self.assertRaises(TypeError):
            s2 << 5.6


if __name__ == "__main__":

    unittest.main()