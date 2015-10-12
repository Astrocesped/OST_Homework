#!/usr/local/bin/python3
#
# Lesson 15 "Memory-Mapped Files" Homework Project

__author__ = "cmontesr"

'''
Created on Oct 5, 2015

mmap_file_writer.py: Creates a binary data file through the mmap module
                     by using successively higher indexes for byte
                     data insertion.
'''

import mmap
import struct
import os

RAW_FILENAME = "mmaped_file01"
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

def mmap_file_writer(chunk_size=1000):
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
    f.write(FILESIZE * b'\0')
    f.close()
    # Open it again, on r+ mode, and memory-map it
    f = open(FILENAME, "r+b")
    mapf = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    
    # Insert into the file by increasing indexes and packing bytes
    for segment in range(segments):
        offset = segment * slot_size
        mapf[offset:offset + slot_size] = \
        pack_slot(BYTE_STR for _ in range(slot_size))
    
    # Write the last chunk of bytes, if there was a remainder
    if last_segment:
        offset += slot_size
        SLOT_FORMAT = bytes("{}c".format(last_segment), "utf-8")
        mapf[offset:offset + last_segment] = \
        pack_slot(BYTE_STR for _ in range(last_segment))
    
    # Close the mmaped file and the file itself
    mapf.close()
    f.close()
    
    # Let us know what was the final size and delete the file
    print("mmap's final file size:", os.stat(FILENAME).st_size)
    os.unlink(FILENAME)
    
if __name__ == "__main__":
    mmap_file_writer(chunk_size=100000)