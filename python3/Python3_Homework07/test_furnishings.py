'''
Created on Aug 16, 2015

@author: cmontesr

Unittest module for furnishings.py
'''
import unittest
from furnishings import *

home = []

class TestFurnishings(unittest.TestCase):

    def test_map_the_home(self):
        """
        Tests the home mapping function, map_the_home
        """
        rooms = ("Bedroom", "Kitchen", "Living Room", "Bathroom")
        
        home.append(Bed(rooms[0]))
        home.append(Bookshelf(rooms[0]))
        home.append(Bookshelf(rooms[1]))
        home.append(Bookshelf(rooms[2]))
        home.append(Bookshelf(rooms[3]))
        home.append(Sofa(rooms[0]))
        home.append(Sofa(rooms[2]))
        home.append(Sofa(rooms[3]))
        
        home_map = map_the_home(home)
        
        # Test each dict value's list's length
        self.assertEqual(len(home_map[rooms[0]]), 3)
        self.assertEqual(len(home_map[rooms[1]]), 1)
        self.assertEqual(len(home_map[rooms[2]]), 2)
        self.assertEqual(len(home_map[rooms[3]]), 2)
        
        # Test the presence of the name of certain Furniture subclasses
        self.assertTrue(isinstance(home_map[rooms[0]][0], Bed))
        self.assertTrue(isinstance(home_map[rooms[2]][1], Sofa))
        
        #counter(home)
        

if __name__ == "__main__":
    
    unittest.main()
    
    