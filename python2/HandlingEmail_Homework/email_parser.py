#!/usr/local/bin/python3
#
# Email Creator and Parser
# email_parser.py
#
# 2015 July 20th
#
""" Creates Python emails in different ways. """

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import mimetypes
import os

def create_file_message(recipient_address, *args):
    """ Creates a Python email with file attachments as part of a
    MIME-class message.
    :param recipient_address: Email address of the recipient
    :param *args: List parameter containing filenames
    :return: MIMEMultipart instance
    """
    
    message = MIMEMultipart()
    message["to"] = recipient_address
    
    # Only attach image, plain and html text file types, according to the
    # first element of mimetypes' guess_type method
    for fn in args:
        fn = os.path.normpath(fn)
        
        if not mimetypes.guess_type(fn)[0]:
            continue
        
        if mimetypes.guess_type(fn)[0].find("image") >= 0:
            with open(fn, "rb") as f:
                message.attach(MIMEImage(f.read()))
            
        elif mimetypes.guess_type(fn)[0].find("plain") >= 0:
            with open(fn, "r") as f:
                message.attach(MIMEText(f.read(), "plain"))
                
        elif mimetypes.guess_type(fn)[0].find("html") >= 0:
            with open(fn, "r") as f:
                message.attach(MIMEText(f.read(), "html"))
                
    return message
