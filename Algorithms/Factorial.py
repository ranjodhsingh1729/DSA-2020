# Getting Rid of Recursion Depth (Only for Testing!)
# import sys
# sys.setrecursionlimit(10000)

# Recursive Approach
# Big-O = O(n)
def factorial1(n):
    if n <= 1:
        return 1
    else:
        return n * factorial1(n-1)

# Itterative Approach
# Big-O = O(n)
def factorial2(n):
    factorial = 1
    for num in range(1, n+1):
        factorial *= num
    return factorial
