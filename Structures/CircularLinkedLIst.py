"""
The Circular Linked List Abstract Data Type,
Implementation in Python.
"""

class ListNode:
    def __init__(self, data):
        self.next = None
        self.data = data

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

    def set_next(self, new_next):
        self.next = new_next

    def set_data(self, new_data):
        self.data = new_data

    def __str__(self):
        return str(self.data)


class LinkedList:
    infinity = float("inf")

    def __init__(self):
        self.head = None
        self.tail = None

    def _delete(self, prev, node):
        if self.head == self.tail:
            self.head, self.tail = None, None
        elif node == self.head:
            self.head = self.head.next
            self.tail.next = self.head
        elif node == self.tail:
            prev.next = node.next
            self.tail = prev
        else:
            prev.next = node.next

    def is_empty(self):
        return self.head is None

    def push(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        
        else:
            self.tail.next = item

        self.tail = item
        item.next = self.head

    def pop(self, index=infinity):
        prev = self.head
        temp = self.head

        if self.head is None:
            raise IndexError("Pop From Empty List")

        else:
            counter = 0
            while counter < index:
                prev = temp
                temp = temp.next
                counter += 1
                if temp.next == self.head: break

            self._delete(prev, temp)

        return temp.data

    def index(self, item):
        if isinstance(item, ListNode):
            item = item.data
        
        if self.head is None:
            raise ValueError("Item is not in List")

        else:
            counter = 0
            temp = self.head

            while temp.data != item:
                temp = temp.next
                counter += 1
                if temp.next == self.head: break

            if temp.data == item:
                return counter
            else:
                raise ValueError("Item is not in List")

    def insert(self, index, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)
        
        if self.head is None:
            self.push(item)
        
        else:
            prev = self.head
            temp = self.head

            for _ in range(index):
                prev = temp
                temp = temp.next
                if temp == self.head: break
            else:
                if temp == self.head:
                    self.head = item
                    item.next = temp
                    self.tail.next = self.head
                else:
                    prev.next = item
                    item.next = temp
                return

            prev.next = item
            self.tail = item
            self.tail.next = self.head

    def remove(self, item):
        if self.head is None:
            raise IndexError("Remove From Empty List")
        
        else:
            prev = self.head
            temp = self.head

            counter = 0
            while temp.data != item:
                prev = temp
                temp = temp.next
                counter += 1
                if temp.next == self.head: break

            if temp.data == item:
                self._delete(prev, temp)
                return temp.data
            else:
                raise ValueError("Item not in List")

    def __getitem__(self, key):
        if self.head is None:
            raise IndexError("list index out of range")

        else:
            temp = self.head

            counter = 0
            while counter < key:
                temp = temp.next
                counter += 1
                if temp == self.head:
                    raise IndexError("list assignment index out of range")

            return temp.data

    def __setitem__(self, key, value):
        if self.head is None:
            raise IndexError("list assignment index out of range")

        else:
            temp = self.head

            counter = 0
            while counter < key:
                temp = temp.next
                counter += 1
                if temp == self.head:
                    raise IndexError("list assignment index out of range")

            temp.data = value

    def __len__(self):
        size = 0
        
        if self.head is None:
            return size

        else:
            temp = self.head

            while True:
                size += 1
                temp = temp.next
                if temp == self.head: break

            return size

    def __repr__(self):
        temp = self.head
        string = ""

        string += "["
        while temp:
            string += f"{temp}, "
            temp = temp.next
            if temp == self.head: break
        string += "]"

        return string
