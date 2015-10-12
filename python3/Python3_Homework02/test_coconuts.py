'''
Created on Aug 4, 2015

@author: cmontesr

Tests for coconut.py
'''

import unittest
import coconuts

class TestCoconut(unittest.TestCase):
    
    
    def test_add_coconut(self):
        """
        Tests the Inventory class' add_coconut method.
        """
        inv = coconuts.CoconutInventory()
        
        # Test a wrong type of argument passed to add_coconut
        self.assertRaises(AttributeError, lambda: inv.add_coconut("fail"))
        
        def add_coconut(Coconut, times):
            """
            Helper function to add coconut instances several times.
            :param coconut: Coconut instance
            :param times: Integer telling how many times to add_coconut
            """
            for t in range(times):
                inv.add_coconut(Coconut())
        
        # Add two c1s, one c2, three c3
        add_coconut(coconuts.SouthAsian, 2)
        add_coconut(coconuts.MiddleEastern, 1)
        add_coconut(coconuts.American, 3)
        
        # There should be six coconuts in total
        self.assertEqual(6, len(inv.coco_array))
        
        # Current weight of the inventory should be 19 in total
        self.assertEqual(19.0, inv.total_weight())
        
        # Test the weight of each type of coconut being unique
        # (the generated set should have a length of 3)
        self.assertEqual(3, len(set([c.weight for c in inv.coco_array])))
        

if __name__ == "__main__":
    unittest.main()
