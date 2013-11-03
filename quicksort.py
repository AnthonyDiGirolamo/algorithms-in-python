#!/usr/bin/env python
# coding: utf-8

def quicksort_recursive(array):
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
    if left_index < right_index:
        pivot_index = left_index + int((right_index-left_index)/2)
        new_pivot_index = partition(array, left_index, right_index, pivot_index)
        quicksort(array, left_index, new_pivot_index - 1)
        quicksort(array, new_pivot_index + 1, right_index)

def write_random_data():
    # write out a random list of floats:
    a = [random.random() for i in range(0, 100000)]
    with open("rand_array.pickle", "wb") as f:
        pickle.dump(a, f, pickle.HIGHEST_PROTOCOL)

def random_data():
    data = []
    with open('rand_array.pickle', 'rb') as f:
        data = pickle.load(f)
    return data

if __name__ == '__main__':
    import random
    import pickle
    import timeit

    # write_random_data()

    print("quicksort_recursive:")
    print(timeit.timeit('data = random_data() ; quicksort_recursive(data)',
        setup="from __main__ import random_data, quicksort_recursive", number=10))

    print("quicksort with in place partitioning:")
    print(timeit.timeit('data = random_data() ; quicksort(data,0 , len(data)-1)',
        setup="from __main__ import random_data, partition, quicksort", number=10))


