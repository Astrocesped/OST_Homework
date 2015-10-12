'''
Created on Sep 23, 2015

@author: cmontesr

Unittest module made for def_inspector.py
'''
import unittest
from project_log import *
import project_log
from module_inspector import *

class TestDefInspector(unittest.TestCase):
    
    def test_def_inspector_simple(self):
        """ Tests def_inspect_module's functionality by passing the 
        project_log module. """
        
        self.assertEqual("'def start_logging(filename={0!r}, log_level='INFO', log_format={1!r})'".format(
                         LOG_FILENAME, LOG_FORMAT),
                         def_inspect(project_log))
        
    def test_def_inspector_bigger(self):
        result = """\
'def dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)'
'def dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)'
'def load(fp, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)'
'def loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)'\
"""
        self.assertEqual(result, def_inspect("json"))
        
    def test_def_inspector_error(self):
        " Test erroneous import. "
        self.assertRaises(ImportError, def_inspect, "non-existant")
        

if __name__ == "__main__":
    
    unittest.main()