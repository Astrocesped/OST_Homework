'''
Created on Aug 24, 2015

@author: cmontesr
'''
import unittest
from property_address import *
 
class TestAddresses(unittest.TestCase): 
   
    def setUp(self): 
        self.home = Address( name='Steve Holden',
                             street_address='1972 Flying Circus',
                             city='Arlington', state='VA', zip_code='12345')
       
    def test_name(self): 
        self.assertEqual(self.home.name, 'Steve Holden') 
        self.assertRaises(NameException, setattr, self.home,
                          'name', 'Daniel Greenfeld')  
           
    def test_state(self): 
        self.assertEqual(self.home.state, 'VA')
        self.assertRaises(StateError, setattr, self.home, 'state', 'Not a state')  
        self.home.state = 'CO' 
        self.assertEqual(self.home.state, 'CO')  
        
    def test_zip_code(self):
        self.assertEqual(self.home.zip_code, '12345')
        self.assertRaises(ZipCodeError, setattr, self.home, 'zip_code', '123456')
        self.home.zip_code = '54321'
        self.assertEqual(self.home.zip_code, '54321')
        
        
class TestDifferentConfig(unittest.TestCase):
        
    def setUp(self): 
        self.home = Address( name='Steve Holden',
                             street_address='1972 Flying Circus',
                             city='Arlington', state='VA', zip_code='12345')
        
    def test_different_settings(self):
        """
        Modify the module's global settings by reading a configuration file
        """
        read_config_file("property_address.cfg")

        self.home.state = 'VAN'
        self.assertEqual(self.home.state, 'VAN')
        self.assertRaises(StateError, setattr, self.home, 'state', 'CO')
        
        self.home.zip_code = '12345-6789'
        self.assertEqual(self.home.zip_code, '12345-6789')
        self.assertRaises(ZipCodeError, setattr, self.home, 'zip_code', '12345')
        
       
if __name__ == "__main__":
    
    start_logging("property_address.log")
    unittest.main() 