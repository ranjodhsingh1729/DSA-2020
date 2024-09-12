"""
The Linked List Abstract Data Type,
Implementation in Python.
"""

# ListNode
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

# List
class LinkedList:
    infinity = float("inf")

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        if self.head is None:
            return 0
        else:
            size = 1
            temp = self.head

            while temp.next:
                temp = temp.next
                size += 1

            return size

    def push(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item

        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = item

    def pop(self, index=infinity):
        if self.head is None:
            raise IndexError("Pop From Empty List")

        else:
            prev = self.head
            temp = self.head

            counter = 0
            while temp.next and counter < index:
                prev = temp
                temp = temp.next
                counter += 1

            if temp == self.head:
                self.head = temp.next

            else:
                prev.next = temp.next

    def insert(self, index, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)

        prev = self.head
        temp = self.head
        
        if self.head is None or index == 0:
            self.head = item
            item.next = temp

        else:
            counter = 0
            while temp.next and counter < index:
                prev = temp
                temp = temp.next
                counter += 1
            
            if counter == index:
                prev.next = item
                item.next = temp
            else:
                temp.next = item

    def remove(self, item):
        if self.head is None:
            raise IndexError("Remove From Empty List")

        else:
            prev = self.head
            temp = self.head

            while temp.next:
                if temp.data == item:
                    break
                prev = temp
                temp = temp.next

            if temp.data == item:
                if temp == self.head:
                    self.head = temp.next
                else:
                    prev.next = temp.next
            else:
                raise ValueError("Item not in List")

    def get_index(self, item):
        if self.head is None:
            raise ValueError("Item not in list")

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
                raise ValueError("Item not in list")

    def get_item(self, index):
        if self.head is None:
            raise IndexError("Peek From Empty List")
    
        else:
            temp = self.head

            counter = 0
            while temp.next and counter < index:
                temp = temp.next
                counter += 1

            return temp.data

    def __str__(self):
        temp = self.head
        string = ""

        string += "["
        while temp:
            string += f"{temp}, "
            temp = temp.next
        string += "]"

        return string
