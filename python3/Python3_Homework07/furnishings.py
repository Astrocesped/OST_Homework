#!/usr/local/bin/python3

'''
Created on Aug 17, 2015

@author: cmontesr

furnishings.py: Fills and maps a house's room furniture by using classes.
'''

#################### CLASSES ####################

class Furnishing:
    """
    Superclass to build the furniture in the house.
    """
    def __init__(self, room):
        """
        :param room: String detailing the location of the instance
                    inside the house.
        """
        self.room = room
        
        
class Bed(Furnishing):
    
    def __init__(self, room):
        super().__init__(room)
        
        
class Bookshelf(Furnishing):
    
    def __init__(self, room):
        super().__init__(room)
        

class Sofa(Furnishing):
    
    def __init__(self, room):
        super().__init__(room)
        

class Table(Furnishing):
    
    def __init__(self, room):
        super().__init__(room)
        
        
#################### HELPER FUNCTIONS ####################

def counter(furniture_list):
    """
    Prints an inventory of the Furniture subclasses in a house.
    :param furniture_list: List of Furniture subclass instances
    """
    to_print = {
                "Bed": 0,
                "Bookshelf": 0,
                "Sofa": 0,
                "Table": 0,
                "Other": 0
                }
    
    # Get the class of each instance through its __class__ attribute;
    # keep adding each Class to its corresponding dict key
    for item in furniture_list:
        # Get the name of the class this instance inherits from
        cname = item.__class__.__name__
        
        # If a class not implemented so far, include it in Other
        if cname not in to_print.keys():
            cname = "Other"
            
        to_print[cname] += 1
        
    print("Beds: {0}\nBookshelves: {1}".format(to_print["Bed"],
                                               to_print["Bookshelf"]))
    print("\nSofas: {0}\nTables: {1}".format(to_print["Sofa"],
                                             to_print["Table"]))
    if to_print["Other"]:
        print("\nOther:", to_print["Other"])

def map_the_home(furniture_list):
    """
    Displays the furniture content of each room.
    :param furniture_list: List of Furniture subclass instances
    :return: Dict containing pairs of room: list of Furniture instances
    """
    
    home = {}
    
    for item in furniture_list:
        
        # If the room already exists in the dict, append the
        # furniture instance to its list; else, create new list
        if home.get(item.room):
            home[item.room].append(item)
            continue
        home[item.room] = [item]
        
    return home
