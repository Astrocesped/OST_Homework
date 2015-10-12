#!/usr/local/bin/python3
#
# Lesson 10 "Multi-Threading" Homework Project
#
__author__ = "cmontesr"
'''
Created on Sep 24, 2015

thread_chdir.py: Provides a threading subclass that changes the
                 current working directory.
'''
import threading
import os
from time import sleep
from project_log import start_logging
from logging import info as log_info

# Provide a variable to allow other modules to access active_count without
# importing threading themselves
active_count = threading.active_count

start_logging()

class DirectoryTravelThread(threading.Thread):
    def __init__(self, sleeptime, *args, **kwargs):
        """
        Initializes a new DirectoryTravelThead instance.
        :param path: Filepath to travel to
        """
        threading.Thread.__init__(self, *args, **kwargs)
        self.sleeptime = sleeptime
        
        log_info("New DirectoryTravelThead instance at directory {}".format(
                    os.getcwd()))
    
    def run(self):
        for _ in range(self.sleeptime):
            sleep(1)
            log_info("{0} currently located at directory {1}".format(
                self.name, os.getcwd()))
            
        log_info("{0} has finished execution at directory {1}".format(
                self.name, os.getcwd()))
