#!/usr/bin/env python
# coding: utf-8

# Worst Case:    O(n^2)
# Best Case:     O(n log n)
# Average Case:  O(n log n)

def quicksort_recursive(array):
    """Run a recursive implementation of quicksort on a list

    >>> a = [4,6,7,88,33,2,2,4567,78,4,32,2553,2455,2,45,7,6,332232]
    >>> print(quicksort_recursive(a))
    [2, 2, 2, 4, 4, 6, 6, 7, 7, 32, 33, 45, 78, 88, 2455, 2553, 4567, 332232]
    """

    if len(array) <= 1:
        return array
    less     = []
    greater  = []
    midpoint = int(len(array)/2)
    pivot    = array[midpoint]
    array    = array[:midpoint] + array[midpoint+1:]
    for item in array:
        if item <= pivot:
            less.append(item)
        else:
            greater.append(item)
    return (quicksort_recursive(less) + [pivot] + quicksort_recursive(greater))


def partition(array, left_index, right_index, pivot_index):
    pivot_value        = array[pivot_index]
    array[pivot_index], array[right_index] = array[right_index], array[pivot_index]
    # pivot_value        = array[pivot_index]
    # array[pivot_index] = array[right_index]
    # array[right_index] = pivot_value
    store_index        = left_index
    for i in range(left_index, right_index):
        if array[i] <= pivot_value:
            array[store_index], array[i] = array[i], array[store_index]
            # store_value        = array[store_index]
            # array[store_index] = array[i]
            # array[i]           = store_value
            store_index += 1
    array[store_index], array[right_index] = array[right_index], array[store_index]
    # store_value        = array[store_index]
    # array[store_index] = array[right_index]
    # array[right_index] = store_value
    return store_index

def quicksort(array, left_index, right_index):
    """Run a in-place partitioning implementation of quicksort on a list

    >>> a = [4,6,7,88,33,2,2,4567,78,4,32,2553,2455,2,45,7,6,332232]
    >>> quicksort(a, 0, len(a)-1)
    >>> print(a)
    [2, 2, 2, 4, 4, 6, 6, 7, 7, 32, 33, 45, 78, 88, 2455, 2553, 4567, 332232]
    """

    if left_index < right_index:
        pivot_index = left_index + int((right_index-left_index)/2)
        new_pivot_index = partition(array, left_index, right_index, pivot_index)
        quicksort(array, left_index, new_pivot_index - 1)
        quicksort(array, new_pivot_index + 1, right_index)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
