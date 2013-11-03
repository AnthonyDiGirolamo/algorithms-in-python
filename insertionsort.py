#!/usr/bin/env python
# coding: utf-8

# Worst Case:    O(n^2)
# Best Case:     O(n)
# Average Case:  O(n^2)

def insertionsort(array):
    """Run insertionsort on a list

    >>> a = [45,67,2,3,5,7,898,9,6,5,4,33,3,35566,1]
    >>> insertionsort(a)
    >>> print(a)
    [1, 2, 3, 3, 4, 5, 5, 6, 7, 9, 33, 45, 67, 898, 35566]
    """

    for i in range(1, len(array)):
        value_to_insert = array[i]
        hole_index = i
        while hole_index > 0 and value_to_insert < array[hole_index - 1]:
            array[hole_index] = array[hole_index - 1]
            hole_index -= 1
        array[hole_index] = value_to_insert

if __name__ == "__main__":
    import doctest
    doctest.testmod()
