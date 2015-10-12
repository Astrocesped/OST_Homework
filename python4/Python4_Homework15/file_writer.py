#!/usr/local/bin/python3
#
# Lesson 15 "Memory-Mapped Files" Homework Project

__author__ = "cmontesr"

'''
Created on Oct 5, 2015

file_writer.py: Creates a binary data file through the built-in function
                write() through iteration by chunk size.
'''

import mmap
import struct
import os

RAW_FILENAME = "written_file01"
FILESIZE = 10485760 # Ten megabytes
BYTE_STR = b"c"
SLOT_FORMAT = None

# Normalize filename
FILENAME = os.path.normpath(RAW_FILENAME)

def pack_slot(data_collection):
    """
    Creates binary data by following the SLOT_FORMAT and
    unpacking the received data into struct's pack().
    :param data_collection: List/tuple of iterated byte data
    """
    return struct.pack(SLOT_FORMAT, *data_collection)

def file_writer(chunk_size=1000):
    """
    Generates the file by inserting a set number of bytes,
    defined by BYTE_STR.
    :param chunk_size: Determines the number of bytes each loop iteration
                       will insert into the file
    """
    # Update the SLOT_FORMAT to fit the desired chunk_size
    global SLOT_FORMAT
    SLOT_FORMAT = bytes("{}c".format(chunk_size), "utf-8")
    # Determine the size of bytes that each iteration will write 
    slot_size = struct.calcsize(SLOT_FORMAT)
    # How many times to iterate, depending on the slot_size
    segments = int(FILESIZE / slot_size)
    # Determine the last segment to write
    last_segment = FILESIZE % slot_size
    
    # Write an empty file
    f = open(FILENAME, "wb")
    
    # Insert into the file by iterating through segments
    for _ in range(segments):
        f.write(pack_slot(BYTE_STR for _ in range(slot_size)))
    
    # Write the last chunk of bytes, if there was a remainder
    if last_segment:
        SLOT_FORMAT = bytes("{}c".format(last_segment), "utf-8")
        f.write(pack_slot(BYTE_STR for _ in range(last_segment)))
    
    f.close()
    
    # Let us know what was the final size and delete the file
    print("write()'s final file size:", os.stat(FILENAME).st_size)
    os.unlink(FILENAME)
    
if __name__ == "__main__":
    file_writer(1000000)