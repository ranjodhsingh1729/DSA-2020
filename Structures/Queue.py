from ..Structures.LinkedList import LinkedList

"""
The Queue Abstract Data Type,
Implementation in Python.
"""

class Queue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._items = list()
    
    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self._items)

    def push(self, item):
        if self.size() < self.maxsize:
            self._items.insert(0, item)
        else:
            raise ValueError("Queue Size Limit Reached!")
    
    def pop(self):
        if self.size():
            return self._items.pop()
        else:
            raise ValueError("Pop from empty List!")
    
    def __str__(self):
        return self._items.__str__()
