from ..Structures.Stack import Stack


def divide(exp):
    s = Stack()
    ops = "+-*/"
    index = 0
    counter = 0
    for char in exp:
        if char == "(":
            counter += 1
        if char == ")":
            counter -= 1
        if counter == 0 and char in ops:
            operands = exp[:index], exp[index+1:]
            return operands, char
        index += 1
    


def infix_to_prefix(exp):
    exp = exp.strip()
    exp = exp[1:-1]
    ops = divide(exp)
    if ops:
        operands, operator = ops
    else:
        return exp
    exp = operands[0].strip() +" "+ operands[1].strip() +" "+ operator
    print(exp)
    return infix_to_prefix(exp)

print(infix_to_prefix("(((A + B) * C) - ((D - E) * (F + G)))"))