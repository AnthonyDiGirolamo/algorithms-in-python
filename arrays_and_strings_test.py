#!/usr/bin/env python
import pytest

import pprint
pp = pprint.PrettyPrinter(indent=4).pprint

# @pytest.fixture
# def today():
#     return date.today()

# def test_todos_init(todos):
#     assert len(todos) == 5
#     assert len(todos.todo_items) == 5

def contains_only_unique_chars(chars, max_count=1):
    """Check a string for unique charachters

    Arguments:

        chars:     the string to be checked
        max_count: the number of allowed duplicates

    Examples:

        >>> contains_only_unique_chars("abcdefghijklmnopqrstuvwxyz")
        True
        >>> contains_only_unique_chars("a")
        True
        >>> contains_only_unique_chars("abcdefghhhhhh")
        False
        >>> contains_only_unique_chars("  123456")
        False
    """
    pp(chars)

    # Hash

    character_hash = {}
    for c in chars:
        character_hash[c] = character_hash.get(c, 0) + 1
        if character_hash[c] > max_count:
            return False
    pp(character_hash)
    return True

    # List of Booleans:

    # seen = [False for i in range(256)]
    # for c in chars:
    #     if seen[ord(c)]:
    #         return False
    #     seen[ord(c)] = True
    # return True

    # Store if we've seen a character in a bit
    # only working for a-z

    # seen = 0
    # for c in chars:
    #     # pp(c)
    #     # pp(bin(seen))
    #     # pp(bin((1 << (ord(c) - ord("a")))))
    #     if seen & (1 << (ord(c) - ord("a"))) > 0:
    #         return False
    #     seen |= 1 << (ord(c) - ord("a"))
    # return True

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
