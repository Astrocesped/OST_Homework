'''
Created on Aug 16, 2015

@author: cmontesr

Unittest module for ccn_safety2.py
'''

import unittest
from ccn_safety2 import substitute_ccn

class TestCCNsafety(unittest.TestCase):

    def test_substitute_ccn(self):
        text = """\
Have you ever noticed, in television and movies, that phone numbers and credit cards
are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a 
number that appears to be real, such as 1234-5678-1234-5678, triggers the attention of 
privacy and security experts."""
        
        updated_text = substitute_ccn(text)
        
        # Individual numbers tests
        self.assertTrue("5555-5555-5555-5555" not in updated_text)
        self.assertTrue("1234-5678-1234-5678" not in updated_text)
        
        # Whole text test
        should_be = """\
Have you ever noticed, in television and movies, that phone numbers and credit cards
are obviously fake numbers like 555-123-4567 or CCN REMOVED FOR YOUR SAFETY? It is because a 
number that appears to be real, such as CCN REMOVED FOR YOUR SAFETY, triggers the attention of 
privacy and security experts."""
        
        self.assertEqual(should_be, updated_text)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCCNsafety']
    unittest.main()