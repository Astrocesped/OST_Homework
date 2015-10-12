'''
Created on Sep 14, 2015

@author: cmontesr
'''
import unittest
from timeit import Timer
from groffle import *

mass = 2.5 
density = 12.0

class TestGroffle(unittest.TestCase):
    
    def test_groffle_results(self):
        slow = groffle_slow(mass, density)
        fast = groffle_fast(mass, density)
        faster = groffle_faster(mass, density)
        
        self.assertAlmostEqual(slow / fast, fast / faster)
        
    def test_groffle_times(self):
        
        slow_timer = Timer("total_slow = groffle_slow(mass, density)",
                           "from __main__ import groffle_slow, mass, density")
        
        fast_timer = Timer("total_fast = groffle_fast(mass, density)", 
                           "from __main__ import groffle_fast, mass, density")
        
        faster_timer = Timer("total_fast = groffle_faster(mass, density)", 
                             "from __main__ import groffle_faster, mass, density")
        
        self.assertLess(fast_timer.timeit(number=1000),
                        slow_timer.timeit(number=1000))
        
        self.assertLess(faster_timer.timeit(number=1000),
                        fast_timer.timeit(number=1000))
        
        # Less than a third than gruffle_slow?
        self.assertLess(faster_timer.timeit(number=1000),
                        slow_timer.timeit(number=1000) / 3)
        

if __name__ == "__main__":

    unittest.main()