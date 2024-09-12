# Getting Rid of Recursion Depth (Only for Testing!)
# import sys
# sys.setrecursionlimit(10000)


# Recursive Approach
# Big-O = O(2^n)
def fib1(n):
    if n <= 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


# Another Recursive Approach
# Big-O = O(n)
def fib2(n, a=0, b=1):
    if n == 0:
        return b
    else:
        return fib2(n-1, b, a+b)


# Itterative Approach
# Big-O = O(n)
def fib3(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return b
