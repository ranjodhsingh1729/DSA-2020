# Itterative Approach
# Big-O = O(n)
def sum_of_n_1(n):
    sum = 0
    for num in range(1, n+1):
        sum += num
    return sum


# Constant Approach
# Big-O = O(1)
def sum_of_n_2(n):
    sum = int(n*(n+1)/2)
    return sum
