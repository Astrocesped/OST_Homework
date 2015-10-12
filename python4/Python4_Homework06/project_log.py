'''
Created on Sep 5, 2015

@author: cmontesr

project_log.py: Logs the main module in a package with a generic
                function.
'''
import logging
from os import path

LOG_FILENAME = "project_log.log"
LOG_LEVELS = {
              "DEBUG": logging.DEBUG,
              "INFO": logging.DEBUG,
              "WARNING": logging.WARNING,
              "ERROR": logging.ERROR,
              "CRITICAL": logging.CRITICAL
              }
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"

def start_logging(filename=LOG_FILENAME,
                  log_level="INFO",
                  log_format=LOG_FORMAT):
    """
    Starts basic logging of a module.
    """
    logging.basicConfig(filename=path.normpath(filename),
                        level=LOG_LEVELS[str.upper(log_level)],
                        format=log_format)