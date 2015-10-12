'''
Created on Sep 25, 2015

@author: cmontesr

Unittest module for the Control module of the Python4_Homework11 package
'''
import unittest
import control
import sys
import re
from io import StringIO
from project_log import start_logging, log_info
from timeit import Timer

start_logging()

class TestThreadingRandomSTR(unittest.TestCase):

    def test_console_output_and_time(self):
        " Tests the resulting console output from the framework's output. "
        
        regex_workers = re.compile("(Worker Thread-[\d]+ done[\n]){10}")
        
        saved_output = sys.stdout
        
        try:
            out = StringIO()
            sys.stdout = out
            
            control.main()
            
            output = out.getvalue().strip()
            
            # Due to random nature, separate the presence of console output
            self.assertTrue(regex_workers.match(output))
            self.assertTrue(re.search("Final length of random string: 1000", output))
            self.assertTrue(re.search("Control thread terminating", output))
            self.assertTrue(re.search("Output thread terminating", output))
            
            # Now that console output is nullified, log total time
            timer = Timer("t = control.main()",
                          "from __main__ import control")
            
            log_info("Latest run took {} secs to complete".format(
                        timer.timeit(number=10)))
            
        finally:
            sys.stdout = saved_output
        

if __name__ == "__main__":

    unittest.main()