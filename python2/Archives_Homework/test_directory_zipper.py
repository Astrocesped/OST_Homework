#
# 2015 July 9th
#
""" Test Unit for directory_zipper.py """

import unittest
import directory_zipper
import zipfile
import os
import shutil
import tempfile

class Test_DirectoryZipper(unittest.TestCase):
    def setUp(self):
        """Create a temporary directory with files for the zip tests. """
        self.original_dir = os.getcwd()
        self.temp_dir = tempfile.mkdtemp("test_directory_zipper")
        os.chdir(self.temp_dir)
    
    def test_ZipFilesOnly(self):
        """ Creates files and sub-directories in the current temp folder. """
        
        self.maxDiff = None
        
        # Make the directory to be zipped
        dir_to_zip = os.path.join(self.temp_dir, "target_directory")
        os.mkdir(dir_to_zip)
        
        # Create the filenames to be saved in the directory, prefixed with
        # the name of their parent directory (i.e. target_directory/test1)
        expected = [os.path.join(os.path.basename(dir_to_zip),
                                 "test{0}".format(i)) for i in range(1, 8)]
        
        # Create test files inside the directory to zip
        [open(fn, "w").close() for fn in expected]
        
        # Create a sub-directory too, that should not be zipped
        os.mkdir(os.path.join(dir_to_zip, "directory_to_skip"))
        
        # Zip the current directory through the function
        directory_zipper.zip_files_only(dir_to_zip)
        
        # Open the resulting zip file in read mode
        zip_file = zipfile.ZipFile(dir_to_zip + ".zip")
        self.assertEqual([os.path.normpath(fn) for fn in zip_file.namelist()],
                         expected)
        
        zip_file.close()
    
    def tearDown(self):
        """ Remove the temporary directory, which contains the test zipped
        file and the non-zipped directory. """
        os.chdir(self.original_dir)
        shutil.rmtree(self.temp_dir)
        
if __name__ == "__main__":
    unittest.main()
