'''
Created on Aug 14, 2015

@author: cmontesr

Unittest module for ccn_safety.py
'''

import unittest
from ccn_safety import substitute_ccn

class TestCCNsafety(unittest.TestCase):

    def test_substitute_ccn(self):
        text = """\
Have you ever noticed, in television and movies, that phone numbers and credit cards
are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a 
number that appears to be real, such as 1234-5678-1234-5678, triggers the attention of 
privacy and security experts."""

        
        updated_text = substitute_ccn(text)
        
        # Individual numbers tests
        self.assertFalse("XXX-XXX-4567" in updated_text)
        self.assertTrue("XXXX-XXXX-XXXX-5555" in updated_text)
        self.assertTrue("XXXX-XXXX-XXXX-5678" in updated_text)
        
        # Whole text test
        should_be = """\
Have you ever noticed, in television and movies, that phone numbers and credit cards
are obviously fake numbers like 555-123-4567 or XXXX-XXXX-XXXX-5555? It is because a 
number that appears to be real, such as XXXX-XXXX-XXXX-5678, triggers the attention of 
privacy and security experts."""
        
        self.assertEqual(should_be, updated_text)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCCNsafety']
    unittest.main()