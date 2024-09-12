# Minimum

# Itterative Approach
# Big-O = O(n)
def minimum(array):
    mini = array[0] if len(array) else None
    for item in array:
        if item < mini:
            mini = item
    return mini

# Maximum

# Itterative Approach
# Big-O = O(n)
def maximum(array):
    maxi = array[0] if len(array) else None
    for item in array:
        if item > maxi:
            maxi = item
    return maxi
