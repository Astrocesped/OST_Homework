# Lesson 11 "More on Multi-Threading" Homework Project
#
__author__ = "cmontesr"
'''
Created on Sep 25, 2015

output.py: The output thread for the miniature framework.
'''
identity = lambda x: x

from multiprocessing import Process
from project_log import start_logging, log_info
import sys

class OutThread(Process):
    
    def __init__(self, N, q, sorting=True, *args, **kwargs):
        " Initialize process and save queue reference. "
        Process.__init__(self, *args, **kwargs)
        self.queue = q
        self.workers = N
        self.sorting = sorting
        self.output = []
        
    def run(self):
        " Extract items from the output queue and print until all done. "
        
        while self.workers:
            p = self.queue.get()
            
            if p is None:
                self.workers -= 1
                
            else:
                # This is a real output packet
                self.output.append(p)
        
        start_logging()
        output_txt = "Final length of random string: {}".format(len(self.output))
        print(output_txt)
        log_info(output_txt)
        
        print("Output process terminating")
        sys.stdout.flush()
