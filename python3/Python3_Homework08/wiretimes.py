#!/usr/local/bin/python3
#
# Lesson 8: Consuming and Creating Binary Data Homework Project
#
'''
Created on Aug 18, 2015

@author: cmontesr

wiretimes.py: Reads a binary file, dumped by the wireshark program,
              which follows the format detailed in here:
              http://wiki.wireshark.org/Development/LibpcapFileFormat,
              and found in the same directory as 'wireshark.bin'.
              Prints the timestamp for each packet.
'''

from struct import unpack
import time
import os


def read_wireshark_packets(filename):
    """
    Reads a libcap binary file produced by a networking tool.
    With help of the struc library, determines the timestamp for each
    packet of data of such file.
    :param filename: pathname of the file to be read
    :return: String containing the above detailed information
    """
    # File reader should stop before reaching this integer
    file_size = os.stat(os.path.normpath(filename)).st_size
    # List of strings to return
    to_print = []
    
    # Read the file
    with open(filename, "rb") as f:
        """
        Statements left for personal research. Their purpose is to practice
        byte-reading the first seven global headers. They amount to 24 places.
    
        print("Magic:", unpack("=L", f.read(4)))
        print("Version:", unpack("=h", f.read(2)))
        print("Version:", unpack("=h", f.read(2)))
        print("Thiszone:", unpack("=l", f.read(4)))
        print("Sigfigs:", unpack("=L", f.read(4)))
        print("Snaplength:", unpack("=L", f.read(4)))
        print("Network:", unpack("=L", f.read(4)), "\n")
        print("Current file location:", f.tell(), "\n")
        """
        # Integer to keep the position where the file reader is currently at
        # Skip the global headers (amount of 24)
        current_pos = 24
        packet = 0
        
        # While end of file is not yet reached, read packet by packet
        while True:
            # Jump to a certain position in the file
            f.seek(current_pos)
            
            # Retrieve the timestamp in seconds, ts_sec; add it to the list
            ts_sec, = unpack("=L", f.read(4))
            to_print.append("Packet number: {0}".format(packet))
            
            to_print.append("Timestamp (secs): {0} equivalent to {1}".format(
                            ts_sec, time.ctime(ts_sec)))
            
            # Append to the list the timestamp in microseconds of this packet
            to_print.append("Timestamp in microseconds: {0}\n".format(
                            unpack("=L", f.read(4))[0]))
            
            incl_len, = unpack("=i", f.read(4))
            
            # Add 4 bytes for the 'orig_len' header, 12 for the headers above,
            # and the length of bytes that the packet occupies (incl_len)
            # to the current_pos. Lines left for self-reference:
            # print("Included length:", incl_len)
            # print("Actual length:", unpack("=L", f.read(4)))
            current_pos += 16 + incl_len
            packet += 1
            
            if current_pos >= file_size:
                break
            
    return "\n".join(to_print)

if __name__ == "__main__":
    print(read_wireshark_packets("wireshark.bin"))

