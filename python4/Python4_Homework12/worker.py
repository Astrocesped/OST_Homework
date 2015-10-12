# Lesson 11 "More on Multi-Threading" Homework Project
#
__author__ = "cmontesr"
'''
Created on Sep 25, 2015

worker.py: A sample worker thread that receives input
           through one Queue and routes output through another.
'''
from multiprocessing import Process
import sys

class WorkerThread(Process):
    
    def __init__(self, iq, oq, *args, **kwargs):
        " Initialize thread and save Queue references. "
        Process.__init__(self, *args, **kwargs)
        self.iq, self.oq = iq, oq
        
    def run(self):
        """ Receive (index, character) pairs, process
        and put onto output queue. """
        while True:
            work = self.iq.get()
            if work is None:
                self.oq.put(None)
                print("Worker", self.name, "done")
                self.iq.task_done()
                break
                
            i, c = work
            result = (i, self.process(c)) # This is the "work"
            self.oq.put(result)
            self.iq.task_done()
        sys.stdout.flush()
            
    def process(self, s):
        " Defines how the string is processed to produce a result. "
        return s.upper()