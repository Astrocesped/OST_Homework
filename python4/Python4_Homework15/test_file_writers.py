# Lesson 15 "Memory-Mapped Files" Homework Project

__author__ = "cmontesr"

'''
Created on Oct 6, 2015

test_file_writers.py: Times mmap_file_writer.py and file_writer.py.
'''

from timeit import Timer
from mmap_file_writer import mmap_file_writer
from file_writer import file_writer
from project_log import start_logging, log_info

def main():
    start_logging()
    
    for chunk_size in 1000, 10000, 100000, 1000000:
        w = Timer("file_writer({})".format(chunk_size),
                          "from __main__ import file_writer")
        mm = Timer("mmap_file_writer({})".format(chunk_size),
                           "from __main__ import mmap_file_writer")
        
        wt = "file_writer took {} w/chunks of {}".format(w.timeit(number=1),
                                                         chunk_size)
        mt = "mmap_file_writer took {} w/chunks of {}".format(mm.timeit(number=1),
                                                              chunk_size)
        
        print(wt)
        print(mt)
        log_info(wt)
        log_info(mt)
        
if __name__ == "__main__":
    main()
