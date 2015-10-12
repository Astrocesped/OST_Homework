#!/usr/local/bin/python3
#
# Food Registry Data Verifier and Handler
# food_registry.py
#
# 2015 July 16th
#
""" Handles and verifies the content of the zoo's animals' food data. """

import mysql.connector
from database import login_info

def non_full_fkey_presence(db_cursor, main_table_info, table_to_check_info,
                           nice_name_column=None):
    """ Looks for the presence of every primary key in 'main_table' inside
    the specified column in 'table_to_check' (therefore, a 'foreign' key).
    
    :param db_cursor: A pre-made SQL cursor.
    :param main_table_info: String in format {name of table}.{primary key},
                            where table holds the values to look for
    :param table_to_check_info: String in format {name of table}.{primary key}
                            where table holds the related keys to above
    :param nice_name_column: Column name in main_table for a more friendly
                            display of the list of primary keys returned
    :return: List containing main_table's primary keys not present in
            table_to_check's specified column
    """
    
    # Obtain the main table and the column name that should be a primary
    # key on it, and the table and its corresponding foreign key
    main_table, primary_key = main_table_info.split(".")
    table_to_check, foreign_key = table_to_check_info.split(".")
    
    # Prepare a query for main_table, in case a second column is desired
    main_table_query = "{0}, {1}".format(primary_key, nice_name_column)
    
    # Select current rows in main_table with existing primary keys
    db_cursor.execute("SELECT {0} FROM {1};".format(main_table_query,
                                                    main_table))

    # Dict that will hold the primary key of each row in main_table as a key,
    # and the "nice name" as a value, if desired
    primary_keys = {}

    for key in db_cursor.fetchall():
        if nice_name_column:
            primary_keys[key[0]] = key[1]
        else:
            primary_keys[key[0]] = None
    
    # Select unique rows in the other table, checking for the foreign keys
    db_cursor.execute("""SELECT DISTINCT {0}
                    FROM {1};""".format(foreign_key, table_to_check))
    foreign_keys = set([key[0] for key in db_cursor.fetchall()])
    
    # Return a list with the primary keys in main_table of each element not
    # found in the specified column of table_to_check
    if nice_name_column:
        return [primary_keys[key] for key in primary_keys.keys()
                if key not in foreign_keys] 
    else:
        return [key for key in primary_keys.keys()
                if key not in foreign_keys]

if __name__ == "__main__":
    
    db = mysql.connector.Connect(**login_info)
    cursor = db.cursor()
    
    # Get a list of animal's primary keys not present in food's anid column,
    # displayed with their corresponding name in animal
    result = non_full_fkey_presence(cursor, "animal.id", "food.anid", "name")
    
    if not result:
        print("Success! Every animal has at least one food assigned.")
    else:
        print("The following animals don't have food assigned:",
              ", ".join(result), end=".")
