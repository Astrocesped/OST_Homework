'''
Created on Sep 24, 2015

@author: cmontesr

Unittest module for thread_chdir.py
'''
import unittest
import os
import tempfile
from shutil import rmtree
from thread_chdir import *

class TestThreadChdir(unittest.TestCase):
    
    def test_normal_behavior(self):
        original_path = os.getcwd()
        
        # Make a new temp directory and switch to it
        temp_path = tempfile.mkdtemp("thread_chdir_tempdir")
        os.chdir(temp_path)
        
        current_dir = os.getcwd()
        
        path_list = [
                     os.path.join(current_dir, "one"),
                     os.path.join(current_dir, "two"),
                     os.path.join(current_dir, "three"),
                     os.path.join(current_dir, "four"),
                     os.path.join(current_dir, "five"),
                     os.path.join(current_dir, "six"),
                     ]
        
        # Create the first three directories inside the temp_folder
        for i, path in enumerate(path_list):
            os.makedirs(path)
            if i == 2:
                break
        
        # Create a list of six TestDirectoryAnalizer instances
        threads = thread_list(path_list)
        
        # And run them
        for i, t in enumerate(threads):
            t.start()
            t.join()
            self.assertEqual(os.getcwd(), path_list[i])
            
        # Delete the temp folder
        os.chdir(original_path)
        rmtree(temp_path)


if __name__ == "__main__":
    unittest.main()