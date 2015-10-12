#!/usr/local/bin/python3
#
# Lesson 11 "More on Multi-Threading" Homework Project
#
__author__ = "cmontesr"
'''
Created on Sep 25, 2015

control.py: Creates queues, starts output and worker processes,
            and pushes inputs into the input queue.
'''
from multiprocessing import Queue, JoinableQueue
from output import OutThread
from worker import WorkerThread

from string import ascii_letters
from random import randint
from project_log import start_logging, log_info

def main(workers=10):
    """
    Executes main function of mini-framework's Control thread.
    :param workers: Integer detailing number of worker FIFO threads to employ
    """
    start_logging()
    log_info("New multiprocessing session with {} workers".format(workers))
    
    # Input JoinableQueue and Output Queue
    inq = JoinableQueue(maxsize=int(workers*1.5))
    outq = Queue(maxsize=int(workers*1.5))
    
    ot = OutThread(workers, outq)
    ot.start()
    
    for _ in range(workers):
        w = WorkerThread(inq, outq)
        w.start()
    
    # Create a sequence of a 1000 random alphabetic characters
    random_chars = (ascii_letters[randint(0, 51)] for _ in range(1000))
    
    # Keep input queue loaded for as long as possible
    # Feed the process pool with work units
    for work in enumerate(random_chars):
        inq.put(work)
    
    # Fill the input queue with Nones to shut the worker threads down
    # which terminates the process pool
    for _ in range(workers):
        inq.put(None)
        
    inq.join()
    print("Control process terminating")
    
if __name__ == "__main__":
    main()