from ..Structures.Stack import Stack


# Validate Brackets Using A Stack
# BIG-O = O(n)
def parser(string):
    s = Stack()
    mapping = {"(": ")", "[": "]", "{": "}"}

    for char in string:
        if char in mapping:
            closing = mapping[char]
            s.push(closing)
        
        if char in mapping.values():
            if not s.is_empty() and char == s.peek():
                s.pop()
            else:
                return False
    
    return s.is_empty()
