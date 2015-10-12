#!/usr/local/bin/python3
#
# Test-Driven Development Introduction
# setupDemo.py
#
# 2015 July 4th
#
"""
Demonstration of setUp and tearDown. Extending what was explored in Lesson 3.
"""
import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
        
    def test_1(self):
        " Creates files in the temporary directory, and verifies that only these are inside. "
        filenames = ["this.txt", "that.txt", "the_other.txt"]
        estranged_files = []
        
        for filename in filenames:
            with open(filename, "w") as f:
                f.write("Some text\n")
                
            self.assertTrue(f.closed)
        
        # Now verify that only these three files are in this directory
        for directory_file in os.listdir():
            # If the file is not one of the three we have created previously
            if directory_file not in filenames:
                estranged_files.append(directory_file)
        
        self.assertFalse(estranged_files,
                         "Files in the current directory not supposed to exist:\
                         {0}".format(", ".join(estranged_files)))
            
    def test_2(self):
        " Verify that the current directory is empty. "
        self.assertEqual(glob.glob("*"), [], "Directory not empty")
        
    def test_3(self):
        " Create a binary file of a certain size and verify it is so just afterwards."
        no_bytes = 1000000
        
        # Create the file with a context manager, which closes it after concluding with the suite inside
        with open("binary_file.bin", "wb") as f:
            f.write(os.urandom(no_bytes))
            
        # Verify that the recently created file is indeed one million bytes
        self.assertEqual(os.stat("binary_file.bin").st_size, no_bytes,
                         "Expected size of binary file is incorrect.")
        
    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
        
if __name__ == "__main__":
    unittest.main()
