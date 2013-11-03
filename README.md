algorithms-in-python
====================

Test Runs
---------

### Sorting 100,000 Floats in  Python 2.7.5, 3.3.2 and PyPy 2.1.0

    $ python test_sorting.py
    2.7.5 (default, Oct 25 2013, 11:07:52)
    [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.2.75)]
    python sorted():
    0.430683135986
    quicksort_recursive:
    1.60994386673
    quicksort with in place partitioning:
    1.55121803284
    top_down_mergesort:
    2.62138414383
    heapsort:
    3.60810089111

    $ python3 test_sorting.py
    3.3.2 (default, Oct 21 2013, 12:01:11)
    [GCC 4.2.1 Compatible Apple LLVM 4.2 (clang-425.0.28)]
    python sorted():
    0.1217644480002491
    quicksort_recursive:
    1.187993325998832
    quicksort with in place partitioning:
    1.2979137350012024
    top_down_mergesort:
    2.366787152001052
    heapsort:
    3.2705076370002644

    $ /usr/local/Cellar/pypy/2.1.0/libexec/bin/pypy test_sorting.py
    2.7.3 (480845e6b1dd, Jul 31 2013, 10:58:28)
    [PyPy 2.1.0 with GCC 4.2.1 Compatible Clang Compiler]
    python sorted():
    0.372516155243
    quicksort_recursive:
    0.644681930542
    quicksort with in place partitioning:
    0.456494092941
    top_down_mergesort:
    0.737778902054
    heapsort:
    0.453850030899
