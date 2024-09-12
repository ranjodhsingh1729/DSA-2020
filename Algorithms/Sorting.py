"""
Some Famous Sorting Algorithms,
Implementation in Python.
"""

def bubble_sort(array, reverse=False):
    compare = lambda x, y: x < y if reverse else x > y

    size = len(array)

    for i in reversed(range(size)):
        Complete = True

        for j in range(i):
            if compare(array[j], array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
                Complete = False
        
        if Complete: break


def insertion_sort(array, reverse=False):
    compare = lambda x, y: x < y if reverse else x > y

    size = len(array)

    for i in range(1, size):
        for j in range(0, i):
            if compare(array[j], array[i]):
                array[i], array[j] = array[j], array[i]


def selection_sort(array, reverse=False):
    compare = lambda x, y: x > y if reverse else x < y

    size = len(array)

    for i in range(size):
        index = i
        
        for j in range(i+1, size):
            if compare(array[j], array[index]): index = j

        array[i], array[index] = array[index], array[i]


def quick_sort(array, first, last):
    if first >= last: return

    i, j = first, last
    pivot = (first + last) // 2
    pivot = array[pivot]

    while i <= j:
        while array[i] < pivot: i += 1
        while array[j] > pivot: j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1; j -= 1
    
    quick_sort(array, first, j)
    quick_sort(array, i, last)


Input = list(reversed(range(10)))
print(Input)
quick_sort(Input, 0, 9)
print(Input)
