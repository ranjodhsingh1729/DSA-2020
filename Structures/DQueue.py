from ..Structures.LinkedList import LinkedList

"""
The DQueue Abstract Data Type,
Implementation in Python.
"""

class DQueue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._items = list()

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self._items)

    def push_front(self, item):
        if self.size() < self.maxsize:
            self._items.insert(0, item)
        else:
            raise ValueError("Queue Size Limit Reached!")

    def push_rear(self, item):
        if self.size() < self.maxsize:
            self._items.append(item)
        else:
            raise ValueError("Queue Size Limit Reached!")

    def pop_front(self):
        if self.size():
            return self._items.pop(0)
        else:
            raise ValueError("Pop from empty List!")
    
    def pop_rear(self):
        if self.size():
            return self._items.pop()
        else:
            raise ValueError("Pop from empty List!")

    def __str__(self):
        return str(self._items)
