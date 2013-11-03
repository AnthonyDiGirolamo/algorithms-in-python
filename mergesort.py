#!/usr/bin/env python
# coding: utf-8

def top_down_mergesort(a):
    """Run a top down mergesort on a list a

    >>> a = [4, 6, 8, 3, 5667, 333, 7, 8, 5, 2, 6, 8, 0, 9, 8]
    >>> top_down_mergesort(a)
    >>> print(a)
    [0, 2, 3, 4, 5, 6, 6, 7, 8, 8, 8, 8, 9, 333, 5667]
    """
    b = [0 for i in a]
    top_down_mergesort_split_merge(a, 0, len(a), b)

def top_down_merge(a, ibegin, imiddle, iend, b):
    left_index = ibegin
    right_index = imiddle
    for j in range(ibegin, iend):
        if ((left_index < imiddle) and (right_index >= iend or a[left_index] <= a[right_index])):
            b[j] = a[left_index]
            left_index += 1
        else:
            b[j] = a[right_index]
            right_index += 1

def top_down_mergesort_split_merge(a, ibegin, iend, b):
    if (iend - ibegin) < 2:
        return
    imiddle = int((iend + ibegin)/2)
    top_down_mergesort_split_merge(a, ibegin, imiddle, b)
    top_down_mergesort_split_merge(a, imiddle, iend, b)
    top_down_merge(a, ibegin, imiddle, iend, b)
    for i in range(ibegin, iend):
        a[i] = b[i]

def mergesort(m):
    """Run a mergesort on a list m

    >>> a = [4, 6, 8, 3, 5667, 333, 7, 8, 5, 2, 6, 8, 0, 9, 8]
    >>> print(mergesort(a))
    [0, 2, 3, 4, 5, 6, 6, 7, 8, 8, 8, 8, 9, 333, 5667]
    """
    if len(m) <= 1:
        return m
    left = []
    right = []
    middle = int(len(m)/2)
    for i in range(0, middle):
        left.append(m[i])
    for i in range(middle, len(m)):
        right.append(m[i])
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
