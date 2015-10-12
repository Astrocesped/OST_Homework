'''
Created on Sep 6, 2015

@author: cmontesr

Unittest module for arr_3d.py
'''
import unittest
import arr_3d

class TestArray(unittest.TestCase):

    def array_class_test(self, class_name):
        """
        Creates an instance of the specified class_name. Checks for
        the three-dimensional array to exist.
        :param class_name: Array class to be instanced
        """
        for N in range(4):
            a = class_name(N, N, N)
            orig_len = a.array_len
            
            for i in range(N):
                a[i, i, i] = 1
            
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i, j, k],i==j==k,
                                         "Not equal in {0}".format((i, j, k)))
            
            #Delete the first element, test new length
            if N > 0:
                del a[0, 0, 0]
                self.assertEqual(a.array_len, orig_len - 1)
            

    def test_array_func(self):
        " Tests array-creating function. "
        array = arr_3d.array_func(3, 4, 5)
        
        for i in range(3):
            for j in range(4):
                for k in range(5):
                    self.assertEqual(array[i][j][k], 0)
                    
        for N in range(4):
            a = arr_3d.array_func(N, N, N)
            
            for i in range(N):
                a[i][i][i] = 1
            
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i][j][k], i==j==k)
                        
    def test_list_lists_array(self):
        " Test list of lists array with subscripting notation class. "
        
        self.array_class_test(arr_3d.List_of_lists_array)
        
    def test_single_list_array(self):
        " Test single list array with subscripting notation class. "
        
        self.array_class_test(arr_3d.Single_list_array)
        
    def test_array_list_array(self):
        " Test single list array done with the array module. "
        
        self.array_class_test(arr_3d.Array_module_array)
        
    def test_dict_array(self):
        " Test dict array. "
        
        self.array_class_test(arr_3d.Dict_array)

if __name__ == "__main__":

    unittest.main()