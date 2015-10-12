"""
Contains names used as global settings for email_scheduler.py
"""

import datetime

RECIPIENTS = [
              ("Carlos 1", "info@carlosmontesr.com"),
              ("Carlos 2", "carlosumbreon@gmail.com")
              ]
STARTTIME = datetime.datetime.now().strftime("%d %b %Y %H:%M:%S -0600")
DAYCOUNT = 5