""" Unittest for classFactory.py """

import unittest
from classFactory import build_row

class DBTest(unittest.TestCase):
    
    def setUp(self):        
        C = build_row("user", "id name email")
        self.c = C([1, "Steve Holden", "steve@holdenweb.com"])
        
    def test_attributes(self):
        self.assertEqual(self.c.id, 1)
        self.assertEqual(self.c.name, "Steve Holden")
        self.assertEqual(self.c.email, "steve@holdenweb.com")        
        
    def test_repr(self):
        self.assertEqual(repr(self.c),
                         "user_record(1, 'Steve Holden', 'steve@holdenweb.com')"
                         )
        
    def test_db_retrieval(self):
        import mysql.connector as mysql_conn
        from database import login_info

        """Connect to a database, retrieve information from a table
        and get the same information as when using classFactory's function."""
        db = mysql_conn.Connect(**login_info)
        cursor = db.cursor()
        
        # Retrieve two rows from the table 'animal'
        cursor.execute("""SELECT name, family, weight FROM animal
                        WHERE family='Hyena';""")
        
        first = cursor.fetchone()
        first_test = "animal_record({0!r}, {1!r}, {2!r})".format(
                    first[0], first[1], first[2])
        second = cursor.fetchone()
        second_test = "animal_record({0!r}, {1!r}, {2!r})".format(
                    second[0], second[1], second[2])
        
        # Create generator instance for assertion tests
        animal_table = build_row("animal", "name family weight")
        animal = animal_table.retrieve(animal_table, cursor, "family='Hyena'")
        
        self.assertEqual(first_test, repr(next(animal)))
        self.assertEqual(second_test, repr(next(animal)))
        
        
if __name__ == "__main__":
    unittest.main()
