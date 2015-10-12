#!/usr/local/bin/python3
#
# Class-Creating Function Sample
# classFactory.py
#
# 2015 July 18th
#
"""
classFactory.py: Function that returns tailored classes.
"""

def build_row(table, cols):
    """ Build a class that creates instances of specific rows. """
    
    class DataRow:
        """ Generic data row class, specialized by surrounding function. """
        
        def __init__(self, data):
            """ Uses data and column names to inject attributes. """
            assert len(data) == len(self.cols)
            
            for colname, dat in zip(self.cols, data):
                setattr(self, colname, dat)
                
        def __repr__(self):
            return "{0}_record({1})".format(self.table,
                                            ", ".join([
                                                       "{0!r}".format(getattr(self, c))
                                                       for c in self.cols
                                                       ]))
        def retrieve(self, curs, condition=None):
            """ Retrieves the rows/data from the instance's columns.
            :param curs: MySQL cursor from an existing connection
            :param condition: String containing conditions for the selection
            :return: Yielded DataRow instance with row elements as attrs
            """
            query = "SELECT {0} FROM {1}".format(", ".join(self.cols),
                                                       self.table)
            
            # Add a semicolon to the end of the query, or conditions, if any
            query += " WHERE {0};".format(condition) if condition else ";"
                
            # Execute SQL Selection using the instance's attributes
            curs.execute(query)
            
            for row in curs.fetchall():
                yield DataRow(row)
            
            
    DataRow.table = table
    DataRow.cols = cols.split()
    
    return DataRow
