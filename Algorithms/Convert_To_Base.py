from ..Structures.Stack import Stack


# Convertes A Decimal Integer To A Give Base
# Big-O = O(!)
def convert(num, base):
    digits = "0123456789ABCDEF"
    
    s = Stack()
    div, mod = divmod(num, base)
    s.push(mod)
    
    while div > 0:
        div, mod = divmod(div, base)
        s.push(mod)
    
    res = ""
    while not s.is_empty():
        res += digits[s.pop()]
    
    return res
