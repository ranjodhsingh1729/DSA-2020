from ..Structures.Stack import Stack

# Reverses An Array Using A Stack
# Big-O = O(n)
def reverse(array):
    rev = ""
    s = Stack()
    size = len(array)
    
    for i in range(size):
        s.push(array[i])
    
    for i in range(size):
        rev += s.pop()
    
    return rev
