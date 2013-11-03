#!/usr/bin/env python
# coding: utf-8

def write_random_data():
    # write out a random list of floats:
    a = [random.random() for i in range(0, 10000)]
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
    import sys

    # write_random_data()

    print(sys.version)

    print("insertionsort:")
    print(timeit.timeit('data = random_data() ; insertionsort(data)', setup="from __main__ import random_data ; from insertionsort import insertionsort", number=3))

    print("quicksort_recursive:")
    print(timeit.timeit('data = random_data() ; quicksort_recursive(data)', setup="from __main__ import random_data ; from quicksort import quicksort_recursive", number=3))

    print("quicksort with in place partitioning:")
    print(timeit.timeit('data = random_data() ; quicksort(data,0 , len(data)-1)', setup="from __main__ import random_data ; from quicksort import partition, quicksort", number=3))

    print("mergesort:")
    print(timeit.timeit('data = random_data() ; mergesort(data)', setup="from __main__ import random_data ; from mergesort import mergesort, merge", number=3))

    print("top_down_mergesort:")
    print(timeit.timeit('data = random_data() ; top_down_mergesort(data)', setup="from __main__ import random_data ; from mergesort import top_down_merge, top_down_mergesort, top_down_mergesort_split_merge", number=3))

