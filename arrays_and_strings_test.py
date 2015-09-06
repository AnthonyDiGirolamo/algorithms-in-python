#!/usr/bin/env python
import pytest

import pprint
pp = pprint.PrettyPrinter(indent=4).pprint

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

class LinkedListNode:
    @staticmethod
    def to_list(head):
        yield head.payload
        if head.next_node:
            for node in LinkedListNode.to_list(head.next_node):
                yield node

    @staticmethod
    def to_list_backwards(tail):
        yield tail.payload
        if tail.prev_node:
            for node in LinkedListNode.to_list_backwards(tail.prev_node):
                yield node

    @staticmethod
    def find_and_delete_node(head, payload):
        node = head
        if head.payload == payload:
            return head
        while node.next_node is not None:
            if node.next_node.payload == payload:
                node.next_node           = node.next_node.next_node
                node.next_node.prev_node = node
                return head
            node = node.next_node
        return head

    def __init__(self, payload=None, next_node=None, prev_node=None):
        self.payload = payload
        self.next_node = next_node
        self.prev_node = prev_node

    def tail_node(self):
        node = self
        while node.next_node is not None:
            node = node.next_node
        return node

    def append_to_tail(self, payload=None):
        node = self
        while node.next_node is not None:
            node = node.next_node
        node.next_node = LinkedListNode(payload=payload, prev_node=node)
        return self

    def length(self):
        size = 0
        node = self
        while node.next_node is not None:
            size += 1
            node = node.next_node
        return size

    def nth_to_last_element(self, n):
        p1 = self
        p2 = self
        for i in range(n-1):
            p2 = p2.next_node
        while p2.next_node is not None:
            p1 = p1.next_node
            p2 = p2.next_node
        return p1

    def delete(self):
        # can't delete if the last node
        if self.next_node is None:
            return False
        self.payload = self.next_node.payload
        self.next_node = self.next_node.next_node
        return True

    def __repr__(self):
        return self.payload

    def __str__(self):
        return str(self.payload)

def remove_duplicates(head, allowed_duplicates=1):
    item_counts = {}
    item_counts[head.payload] = 1
    node = head
    while node.next_node is not None:
        item_counts[node.next_node.payload] = item_counts.get(node.next_node.payload, 0) + 1
        if item_counts[node.next_node.payload] > allowed_duplicates:
            if node.next_node is None:
                node.next_node = None
            else:
                # skip the duplicate
                node.next_node = node.next_node.next_node
                if node.next_node is not None:
                    node.next_node.prev_node = node # for double linked
        else:
            node = node.next_node
    return head

@pytest.fixture
def linked_list():
    l = LinkedListNode(1).append_to_tail(2).append_to_tail(3)
    return l

@pytest.fixture
def linked_list_with_duplicates():
    payloads = "a b c a a d".split()
    l = LinkedListNode(payloads[0])
    for p in payloads[1:]:
        l.append_to_tail(p)
    return l

def test_append_to_tail(linked_list):
    assert linked_list.payload == 1
    assert linked_list.next_node.payload == 2
    assert linked_list.next_node.next_node.payload == 3
    assert linked_list.next_node.next_node.next_node == None
    assert linked_list.next_node.prev_node.payload == 1

def test_to_list(linked_list):
    assert [p for p in LinkedListNode.to_list(linked_list)] == [1,2,3]

def test_to_list_backwards(linked_list):
    assert [p for p in LinkedListNode.to_list_backwards(linked_list.tail_node())] == [3,2,1]

def test_delete_node(linked_list):
    assert [p for p in LinkedListNode.to_list(LinkedListNode.find_and_delete_node(linked_list, 2))] == [1,3]

def test_remove_duplicates(linked_list_with_duplicates):
    n = linked_list_with_duplicates
    remove_duplicates(n)
    ll = LinkedListNode.to_list(n)
    assert [p for p in ll] == "a b c d".split()

def test_remove_duplicates2(linked_list_with_duplicates):
    n = linked_list_with_duplicates
    n.append_to_tail('d')
    remove_duplicates(n)
    ll = LinkedListNode.to_list(n)
    assert [p for p in ll] == "a b c d".split()
    ll = LinkedListNode.to_list_backwards(n.tail_node())
    assert [p for p in ll] == "d c b a".split()

@pytest.fixture
def alphabet():
    payloads = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    l = LinkedListNode(payloads[0])
    for p in payloads[1:]:
        l.append_to_tail(p)
    return l

def test_nth_to_last_element(alphabet):
    assert alphabet.nth_to_last_element(3).payload == "x"

def test_delete(alphabet):
    n = alphabet
    for i in range(6-1):
        n = n.next_node
    n.delete()
    alphabet.delete()
    l = LinkedListNode.to_list(alphabet)
    assert [p for p in l] == "b c d e g h i j k l m n o p q r s t u v w x y z".split()

def number_list(nstring):
    payloads = [int(n) for n in nstring.split()]
    number = LinkedListNode(payloads[0])
    for p in payloads[1:]:
        number.append_to_tail(p)
    return number

def sum_numbers(n1, n2):
    p1 = n1
    p2 = n2
    n3 = LinkedListNode()
    n  = n3
    carry = 0
    while p1 is not None or p2 is not None:
        s = int(
            (p1.payload if p1 else 0) +
            (p2.payload if p2 else 0))
        ones_place = int(s % 10) + carry
        carry      = int(s / 10)
        n.payload = ones_place
        if p1:
            p1 = p1.next_node
        if p2:
            p2 = p2.next_node
        if p1 or p2:
            n.next_node = LinkedListNode()
            n = n.next_node
    return n3

def test_add_numbers():
    n1 = number_list("3 1 5")
    n2 = number_list("5 9 2")
    n3 = sum_numbers(n1, n2)
    n3_list = [p for p in LinkedListNode.to_list(n3)]
    print(n3_list)
    assert n3_list == [8, 0, 8]

    n1 = number_list("1 5")
    n2 = number_list("5 9 2")
    n3 = sum_numbers(n1, n2)
    n3_list = [p for p in LinkedListNode.to_list(n3)]
    print(n3_list)
    assert n3_list == [6, 4, 3]


# def test_pytest_exceptions():
#     with pytest.raises(ZeroDivisionError) as exception_info:
#         1 / 0
#     assert 'integer division or modulo by zero' in str(exception_info.value)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
