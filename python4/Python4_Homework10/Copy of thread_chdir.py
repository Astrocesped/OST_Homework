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
from errno import EEXIST
from time import sleep
from project_log import start_logging
from logging import info as log_info
from logging import error as log_error

start_logging()

class DirectoryTravelThread(threading.Thread):
    def __init__(self, path, sleeptime, *args, **kwargs):
        """
        Initializes a new DirectoryTravelThead instance.
        :param path: Filepath to travel to
        """
        threading.Thread.__init__(self, *args, **kwargs)
        self.directory = os.path.normpath(path)
        self.sleeptime = sleeptime
        
        log_info("New DirectoryTravelThead. Path: {0}".format(self.directory))
    
    def run(self):
        # Change the current working directory to the instance var directory
        try:
            os.chdir(self.directory)
            log_info("Current working directory: {0}".format(self.directory))
        
        # Create the directory if it doesn't exist
        except FileNotFoundError:
            log_info("{0} doesn't exist. Creating it.".format(self.directory))
            
            # Try to make a new directory; check for possible errors
            try:
                os.makedirs(self.directory)
                os.chdir(self.directory)
                log_info("Created and moved to {}".format(self.directory))
                
            except OSError as e:
                # Ignore error if the directory already exists; otherwise...
                if e.errno != EEXIST:
                    log_error(e)
                    raise
            
            except FileNotFoundError as e:
                log_error(e)
                raise


def thread_list(path_list):
    """
    Takes list of filepaths to create DirectoryTravelThread as many instances.
    :param path_list: List of directories to be accessed
    :return: List of DirectoryTravelThread instances
    """
    log_info("Creating a new list of DirectoryTravelThread instances")
    return [DirectoryTravelThread(path_list[i]) for i in range(len(path_list))]