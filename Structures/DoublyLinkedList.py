"""
The Doubly Linked List Abstract Data Type,
Implementation in Python.
"""

class ListNode:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def get_data(self):
        return self.data

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev

    def set_data(self, new_data):
        self.data = new_data

    def __str__(self):
        return str(self.data)


class LinkedList:
    infinity = float("inf")

    def __init__(self):
        self.head = None
        self.tail = None

    def _delete(self, node):
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

        elif node == self.tail:
            self.tail = node.prev
            node.prev.next = None

        else:
            node.prev.next = node.next

        node.prev = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        
        else:
            self.tail.next = item
            item.prev = self.tail

        self.tail = item

    def pop(self, index=infinity):
        if self.head is None:
            raise IndexError("Pop From Empty List")

        else:
            temp = self.head

            counter = 0
            while temp.next and counter < index:
                temp = temp.next
                counter += 1

            self._delete(temp)

    def index(self, item):
        if self.head is None:
            raise ValueError("Item is not in list")

        else:
            temp = self.head

            counter = 0
            while temp.next:
                if temp.data == item:
                    break
                temp = temp.next
                counter += 1

            if temp.data == item:
                return counter
            else:
                raise ValueError("Item is not in list")

    def insert(self, index, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)

        temp = self.head

        if self.head is None:
            self.head = item
            self.tail = item

        elif index == 0:
            self.head = item
            item.next = temp
            temp.prev = item

        else:
            counter = 0
            while temp.next and counter < index:
                temp = temp.next
                counter += 1

            if counter == index:
                prev = temp.prev
                prev.next = item
                item.next = temp
                item.prev = prev
                temp.prev = item
            else:
                temp.next = item
                item.prev = temp
                self.tail = item

    def remove(self, item):
        if self.head is None:
            raise IndexError("Remove From Empty List")
        
        else:
            temp = self.head

            while temp.next:
                if temp.data == item:
                    break
                temp = temp.next

            if temp.data == item:
                self._delete(temp)
                return temp.data
            else:
                raise ValueError("Item not in List")

    def __getitem__(self, key):
        if self.head is None:
            raise IndexError("list index out of range")

        else:
            temp = self.head

            counter = 0
            while temp.next and counter < key:
                temp = temp.next
                counter += 1
            
            if counter == key:
                return temp.data
            else:
                raise IndexError("list index out of range")

    def __setitem__(self, key, value):
        if self.head is None:
            raise IndexError("list index out of range")

        else:
            temp = self.head

            counter = 0
            while temp.next and counter < key:
                temp = temp.next
                counter += 1
            
            if counter == key:
                temp.data = value
            else:
                raise IndexError("list index out of range")

    def __len__(self):
        if self.head is None:
            return 0
        else:
            size = 1
            temp = self.head

            while temp.next:
                temp = temp.next
                size += 1

            return size

    def __repr__(self):
        string = ""

        temp = self.head
        string += "["
        while temp:
            string += f"{temp}, "
            temp = temp.next
        string += "]"

        return string
