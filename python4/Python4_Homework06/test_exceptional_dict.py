'''
Created on Sep 13, 2015

@author: cmontesr
'''
import unittest
from exceptional_dict import *

class TestExceptionalDict(unittest.TestCase):

    def test_erroneous_entries(self):
        t_dict = ExceptionalDict("nothing")
        
        # Insert 10 entries into the dict
        for i in range(10):
            t_dict["value" + str(i)] = i
            self.assertEqual(t_dict["value" + str(i)], i)
        
        # Query an inexistent key
        self.assertEqual(t_dict["valueXX"], "nothing")


if __name__ == "__main__":
    
    unittest.main()