# 2015 July 5th
#
""" Test Case for directory_analyzer.py """

import unittest
import directory_analyzer
import os
import tempfile
import shutil

class TestDirectoryAnalizer(unittest.TestCase):
    def setUp(self):
        """ Creates a temporary directory for testing; moves current
        working path to the newly created. """
        
        # Create the temporary directory
        self.original_path = os.getcwd()
        self.temp_path = tempfile.mkdtemp("directory_analyzer_temp")
        os.chdir(self.temp_path)
        
        # Create several files of different types
        self.temp_files = ["test1.bin", "test2.txt", "test3.doc", "test4.bin"]
        for fn in self.temp_files:
            f = open(fn, "w")
            f.close()
        
        # Dict to be created from the directory analysis
        self.file_dict = {'bin': 2, 'txt': 1, 'doc': 1}
        
    def test_directory_analysis(self):
        """ Test directory file extension count. """
        
        # Create a bogus directory that shouldn't be retrieved in the dict
        os.mkdir("bogus.bogus")
        
        self.assertEqual(directory_analyzer.extension_count_dict(),
                         self.file_dict)
        
    def test_dict_to_str(self):
        """ Test the dict_to_str function, with the existing files. """
        
        dict_to_str = """\
-- Extension --- ---- Count -----
             bin                2
             doc                1
             txt                1\
"""
        self.assertEqual(directory_analyzer.dict_to_str(self.file_dict,
                                                        ["Extension",
                                                         "Count"]),
                         dict_to_str)
        
    def tearDown(self):
        """ Restores the current working directory
        and deletes the temporary one and its contents. """
        os.chdir(self.original_path)
        shutil.rmtree(self.temp_path)
        
if __name__ == "__main__":
    unittest.main()