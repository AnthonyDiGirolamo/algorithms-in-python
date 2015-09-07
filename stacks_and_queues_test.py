#!/usr/bin/env python
import pytest
import pdb
import pprint
pp = pprint.PrettyPrinter(indent=4).pprint

class Node:
    def __init__(self, data=None, n=None):
        self.data = data
        self.n = n

    def to_list(self):
        yield self.data
        if self.n:
            for node in self.n.to_list():
                yield node


class Stack:
    def __init__(self, top_data=None):
        self.top = None
        if top_data:
            self.top = Node(top_data)

    def is_empty(self):
        return self.top == None

    def push(self, data):
        new = Node(data)
        if self.top:
            new.n = self.top
        self.top = new
        return self

    def pop(self):
        if self.top:
            d = self.top.data
            self.top = self.top.n
            return d
        return None

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def to_list(self):
        return [p for p in self.top.to_list()]

    def __str__(self):
        return str(self.to_list())

    def stack_sort(self):
        r = Stack()
        while not self.is_empty():
            d = self.pop()
            while (not r.is_empty()) and r.peek() > d:
                self.push(r.pop())
            r.push(d)
        self.top = r.top
        return self

def test_stack_push_pop():
    s = Stack()
    s.push(1).push(2).push(3)
    assert s.to_list() == [3, 2, 1]
    s.pop()
    assert s.to_list() == [2, 1]

class Queue:
    def __init__(self, data=None):
        self.first = None
        self.last = None
        if data is not None:
            self.enq(data)

    def enq(self, data):
        if self.first is None:
            self.last = Node(data)
            self.first = self.last
        else:
            self.last.n = Node(data)
            self.last = self.last.n
        return self

    def deq(self):
        if self.first is not None:
            d = self.first.data
            self.first = self.first.n
            return d
        return None

    def is_empty(self):
        return self.first == None

    def peek(self):
        if self.is_empty():
            return None
        return self.first.data

    def to_list(self):
        return [p for p in self.first.to_list()]

    def __str__(self):
        return str(self.to_list())

def test_queue_enq_deq():
    q = Queue()
    q.enq(1).enq(2).enq(3)
    assert q.to_list() == [1, 2, 3]
    assert q.peek() == 1
    q.deq()
    assert q.to_list() == [2, 3]

class QueueStack:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    def enq(self, data):
        self.stack1.push(data)
        return self
    def deq(self):
        if self.stack1.is_empty():
            return self.stack2.pop()
        while not self.stack1.is_empty():
            self.stack2.push( self.stack1.pop() )
        return self.stack2.pop()

def test_queuestack_enq_deq():
    q = QueueStack()
    q.enq(1).enq(2).enq(3)
    assert q.stack1.to_list() == [3, 2, 1]
    assert q.stack2.is_empty() == True

    assert q.deq() == 1
    assert q.stack1.is_empty() == True
    assert q.stack2.to_list() == [2, 3]

    assert q.deq() == 2
    assert q.stack1.is_empty() == True
    assert q.stack2.to_list() == [3]

    assert q.deq() == 3
    assert q.stack1.is_empty() == True
    assert q.stack2.is_empty() == True

def test_stack_sort():
    s = Stack()
    for n in [int(n) for n in "4 8 6 7 9 3 5 2 0 1".split()]:
        s.push(n)
    s.stack_sort()
    assert s.to_list() == [int(n) for n in "9 8 7 6 5 4 3 2 1 0".split()]

# def test_pytest_exceptions():
#     with pytest.raises(ZeroDivisionError) as exception_info:
#         1 / 0
#     assert 'integer division or modulo by zero' in str(exception_info.value)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
