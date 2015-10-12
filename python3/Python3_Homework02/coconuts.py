#!/usr/local/bin/python3
#
# Coconut Inventory
# coconuts.py
#
"""
Coconut classes and subclasses; provides an inventory of them
and their individual properties through classes.
"""

class Coconut:
    pass
        

class SouthAsian(Coconut):
    weight = 3
    
    
class MiddleEastern(Coconut):
    weight = 2.5
    
    
class American(Coconut):
    weight = 3.5
    

class CoconutInventory:
    """
    Keeps a collection of Coconut objects.
    """
    def __init__(self):

        self.coco_array = []
    
    def add_coconut(self, c):
        """
        Appends a new Coconut object to the inventory.
        :param c: Coconut instance
        :return: None
        """
        if isinstance(c, Coconut):
            self.coco_array.append(c)
            
        else:
            raise AttributeError("Only Coconut objects can be entered")

    def total_weight(self):
        """
        Gives total weight (sum of each object's weight) of the inventory.
        :return: Float sum of the Coconut instances' weight
        """
        return sum([c.weight for c in self.coco_array])
