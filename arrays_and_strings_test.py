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

def is_uniform(iterable):
    return iterable.count(iterable[0]) == len(iterable)

def is_anagram(*strings):
    """Check if multiple strings are anagrams or not

    Examples:

        >>> is_anagram("race", "cear")
        True
        >>> is_anagram("awesome", "emosewa")
        True
        >>> is_anagram("racecar", "racecar")
        True
        >>> is_anagram("aaaaaaaaaaa", "bbbbbbb")
        False
        >>> is_anagram("crap", "carp")
        True
        >>> is_anagram("crap", "carp", "prac")
        True
        >>> is_anagram("crap", "carp", "prac", "stuf")
        False
        >>> is_anagram("foo", "bar")
        False
    """

    # Count each character

    character_counts = []
    for word_index, word in enumerate(strings):
        character_counts.append({})
        for index, c in enumerate(word):
            character_counts[word_index][c] = character_counts[word_index].get(c, 0) + 1
    for letter in character_counts[0].keys():
        letter_counts = [w.get(letter, None) for w in character_counts]
        if not is_uniform(letter_counts):
            return False
    return True

    # Sorting the strings

    # sorted_words = [sorted(word) for word in strings]
    # return sorted_words.count(sorted_words[0]) == len(sorted_words)

    # return sorted(word1) == sorted(word2)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
