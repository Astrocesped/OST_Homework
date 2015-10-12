#!/usr/local/bin/python3
#
# Directory Zipper
# directory_zipper.py
#
# 2015 July 10th
#
""" Compresses directories into zip files in different ways. """

import zipfile
import os
import glob

def zip_files_only(path):
    """ Compresses a directory and its containing files into a zip file.
    Sub-directories and non-file elements are ignored.
    :param path: Directory to be compressed
    :return: None
    """
    # Normalize the path's name
    path = os.path.normpath(path)
    
    # Create a compressed zip file that will have the same basename as path
    zip_file = zipfile.ZipFile(os.path.basename(path) + ".zip",
                               "w", zipfile.ZIP_DEFLATED)
    
    # Travel to the parent (../) of path to have relative names of each file
    original_dir = os.getcwd()
    os.chdir(os.path.split(path)[0])
    
    # Retrieve the filenames inside the path, if they are actual files only
    files_inside = [fn for fn in glob.glob(os.path.join(
                    os.path.basename(path),"*")) if os.path.isfile(fn)]
    
    # Write the files into the newly created zip file
    [zip_file.write(fn) for fn in files_inside]
    
    zip_file.close()
    
    # Go back to the original directory
    os.chdir(original_dir)
