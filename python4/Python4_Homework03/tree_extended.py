#!/usr/local/bin/python3
#
# Lesson 03: "Delegation and Composition" Homework
#
__author__ = "cmontesr"
'''
Created on Sep 7, 2015

tree_extended.py: Expands the logic of the Tree class found in
                  Lesson 03, so it takes extra attributes to be
                  stored and a find() method.
'''

from project_log import start_logging
from logging import info as log_info
from logging import error as log_error

start_logging()

class Tree:
    """
    Displays use of delegation and recursiveness.
    """
    def __init__(self, key, data=None):
        """
        Create a new Tree object with empty L & R subtrees.
        :param key: Object to be used as the identifier/key of this node
        :param data: Data to be associated with this node
        """
        self.key = key
        self._data = data
        self.left = self.right = None
        
        log_info("New Tree node with key {0} and associated data: {1}".format(
                key, data))
        
    def find(self, key, recursive=False):
        """
        Locates a node and returns the data associated with it.
        :param key: Node identifier
        :return: _data associated with the node
        """
        
        # result keeps the value returned by each recursive use of find()
        result = None
        
        if self.key == key:
            # Key was found, save this data
            result = self._data
            if not result:
                result = _NoDataNode()
            
            log_info("Found value {0} for node {1}".format(result, key))
        
        if not result and self.left:
            for _ in self.left.walk():
                result = self.left.find(key, True)
                if result:
                    break
                
        if not result and self.right:
            for _ in self.right.walk():
                result = self.right.find(key, True)
                if result:
                    break
        
        if isinstance(result, _NoDataNode) and not recursive:
            # The key was found, but it had no data associated
            log_info("Search done, no data inside node {0}".format(key))
            return None
            
        elif not result and not recursive:
            # No key was found
            msg = "No node with key '{0}' was found".format(key)
            log_error(msg)
            raise KeyError(msg)
                
        return result
    
    def insert(self, key, data=None):
        """
        Inserts a new element into the tree in the correct position.
        :param key: Object to be used as the identifier/key of this node
        """
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Tree(key, data)
        
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Tree(key, data)
            
        else:
            msg = "Attempt to insert a duplicate key node"
            log_error(msg)
            raise ValueError(msg)
        
    def walk(self):
        """
        Generate the keys from the tree in sorted order.
        """
        if self.left:
            for n in self.left.walk():
                yield n
                
        yield self.key
            
        if self.right:
            for n in self.right.walk():
                yield n

class _NoDataNode:
    """
    Custom empty class in case finding existing nodes with no data associated.
    """
    pass