'''
Created on Sep 9, 2015

@author: cmontesr
'''
import unittest
from tree_extended import *

class TestTreeExtended(unittest.TestCase):

    def setUp(self):
        self.t = Tree("L")
        
        # Insert several nodes in the Tree's main node
        for letter in "ACFEHNRTWZ":
            self.t.insert(letter)
            
    def test_succesful_find(self):
        # Insert nodes with associated data, then look for them
        self.t.insert("G", "something")
        self.t.insert("X", 6)
        
        self.assertEqual(self.t.find("G"), "something")
        self.assertEqual(self.t.find("X"), 6)
        
    def test_unsuccessful_find(self):
        # Non-existing key, and find key without any data associated
        self.assertRaises(KeyError, self.t.find, "null")
        self.assertEqual(self.t.find("A"), None)


if __name__ == "__main__":

    unittest.main()