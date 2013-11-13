#!/usr/bin/env python
# coding=utf-8

class HashTable:
    """Simple Hash table implementation using open addressing for collisions

    >>> h = HashTable()
    >>> h["set"] = "value"
    >>> h["set"]
    'value'
    """

    def __init__(self, initial_size=300):
        self.array = [None for i in range(0, initial_size)]
        self.size = len(self.array)
        self.count = 0

    def __getitem__(self, key):
        index = self.next_occupied_index(key)
        return self.array[index]

    def __setitem__(self, key, value):
        index = self.next_available_index(key)
        if self.array[index] is None:
            self.array[index] = value
            self.count += 1
        else:
            raise "Collision"

    def _hash(self, key):
        return (hash(key) & self.size)

    def next_occupied_index(self, key):
        index = self._hash(key)
        if index >= self.size or index < 0:
            index = 0
        while index < self.size and self.array[index] is None:
            index += 1
        return index

    def next_available_index(self, key):
        index = self._hash(key)
        if index >= self.size or index < 0:
            index = 0
        while index < self.size and self.array[index] is not None:
            index += 1
        return index

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


