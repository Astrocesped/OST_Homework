#
# 2015 July 11th
#
""" Tests the operation functions of gui_entry_adder.py """

import unittest
import gui_entry_adder

class Test_GUIOperations(unittest.TestCase):
    
    def test_float_adder(self):
        """ Several input tests for the float adder function. """
        self.assertEqual(10.4, gui_entry_adder.add_input(4.5, 5.9))
        self.assertAlmostEqual(3.5e-07, gui_entry_adder.add_input(3e-7, 5e-8))
        self.assertAlmostEqual(.000014,
                                gui_entry_adder.add_input(.000005, .000009),
                                2)
        self.assertAlmostEqual(3.1416,
                               gui_entry_adder.add_input("2.5310", ".6106"))
        self.assertEqual("***ERROR***",
                         gui_entry_adder.add_input("test", []))

if __name__ == "__main__":
    unittest.main()