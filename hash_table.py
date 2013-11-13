#!/usr/bin/env python
# coding=utf-8

class HashTable:
    """Simple Hash table implementation using open addressing for collisions

    >>> h = HashTable()
    >>> h["foo"] = "bar"
    >>> h["foo"]
    'bar'
    >>> h["foo"] = "baz"
    >>> h["foo"]
    'baz'
    """

    def __init__(self, initial_size=300):
        self.array = [None for i in range(0, initial_size)]
        self.size = len(self.array)
        self.count = 0

    def __getitem__(self, key):
        index = self._hash(key)
        if index >= self.size or index < 0:
            index = 0
        while index < self.size and self.array[index][0] != key:
            index += 1
        return self.array[index][1]

    def __setitem__(self, key, value):
        index = self._hash(key)
        if index >= self.size or index < 0:
            index = 0
        while index < self.size and self.array[index] is not None:
            if self.array[index][0] == key:
                break
            index += 1
        self.array[index] = (key, value)
        self.count += 1

    def _hash(self, key):
        return (hash(key) & self.size)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


