"""
Stack Abstract Data Type,
Implementation in Python.
"""

# Class Stack.
class Stack:
    """
    Class Representing A Stack Object.

    Functions Supported:- is_empty, push, pop, peek, size.
    """
    # Constructor
    def __init__(self):
        self._items = []
    
    # Returns True/False Wheather The Stack is Empty?
    def is_empty(self):
        return self._items == []
    
    # Return The Size of The Stack.
    def size(self):
        return len(self._items)
    
    # Adds An Item On Top of The Stack.
    def push(self, item):
        self._items.append(item)
    
    # Removes An Item From Top of The Stack.
    def pop(self):
        return self._items.pop()
    
    # Returns The Item Currrenty On Top of The Stack.
    def peek(self):
        return self._items[-1]
    
    # __str__ Representation for Printing
    def __str__(self):
        return str(self._items)
