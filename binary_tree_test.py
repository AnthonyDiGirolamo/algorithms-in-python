#!/usr/bin/env python
# coding=utf-8

import pytest
import pdb
import pprint
pp = pprint.PrettyPrinter(indent=4).pprint


#           Average     Worst
# Space     O(n)        O(n)
# Search    O(log n)    O(n)
# Insert    O(log n)    O(n)
# Delete    O(log n)    O(n)

class Node:
    """Binary Search Tree Node class

    >>> bstree = BinaryTree(12)
    >>> for i in [5, 18, 2, 9, 15, 19, 13, 17]:
    ...     bstree.insert(i)
    >>> bstree.root.print_in_order()
    2
    5
    9
    12
    13
    15
    17
    18
    19
    >>> [node.payload for node in bstree.root.in_order_walk()]
    [2, 5, 9, 12, 13, 15, 17, 18, 19]
    >>> bstree.search(5)
    5
    >>> bstree.search(99)
    """

    def __init__(self, payload, left=None, right=None, parent=None):
        self.payload = payload
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return repr(self.payload)

    def search(self, data):
        node = self
        while node and node.payload != data:
            if data < node.payload:
                node = node.left
            else:
                node = node.right
        return node
        # Recursive
        # if data == self.payload:
        #     return self
        # elif data < self.payload:
        #     return self.left.search(data) if self.left else None
        # else:
        #     return self.right.search(data) if self.right else None

    def print_in_order(self):
        if self.left:
            self.left.print_in_order()
        print(self.payload)
        if self.right:
            self.right.print_in_order()

    def __str__(self, depth=0):
        """Print simple representation of a tree

        >>> bstree = BinaryTree(12)
        >>> for i in [5, 18, 2, 9, 15, 19, 13, 17]:
        ...     bstree.insert(i)
        >>> print(bstree.root)
                19
            18
                    17
                15
                    13
        12
                9
            5
                2
        <BLANKLINE>
        """
        # 12
        # ├-- 18
        # |   ├-- 19
        # |   └-- 15
        # |       ├-- 17
        # |       └-- 13
        # └-- 5
        #     ├-- 9
        #     └-- 2
        s = ""
        if self.right:
            s += self.right.__str__(depth+1)
        s += depth*"    " + str(self.payload) + "\n"
        if self.left:
            s += self.left.__str__(depth+1)
        return s

    def in_order_walk(self):
        if self.left:
            for node in self.left.in_order_walk():
                yield node
        yield self
        if self.right:
            for node in self.right.in_order_walk():
                yield node

    def minimum(self):
        """ Return the minimum node from self

        >>> bstree = BinaryTree(12)
        >>> for i in [5, 18, 2, 9, 15, 19, 13, 17]:
        ...     bstree.insert(i)
        >>> bstree.minimum()
        2
        """

        node = self
        while node.left is not None:
            node = node.left
        return node

    def maximum(self):
        """ Return the maximum node from self

        >>> bstree = BinaryTree(12)
        >>> for i in [5, 18, 2, 9, 15, 19, 13, 17]:
        ...     bstree.insert(i)
        >>> bstree.maximum()
        19
        """

        node = self
        while node.right is not None:
            node = node.right
        return node

class BinaryTree:

    def __init__(self, root_payload=None):
        self.root = None
        if root_payload:
            self.root = Node(root_payload)

    def minimum(self):
        return self.root.minimum()

    def maximum(self):
        return self.root.maximum()

    def search(self, data):
        return self.root.search(data)

    def insert(self, payload):
        """
        >>> bstree = BinaryTree()
        >>> for i in [12, 5, 18, 2, 9, 15, 19, 13, 17]:
        ...     bstree.insert(i)
        >>> bstree.root.payload
        12
        >>> bstree.root.left.payload
        5
        >>> bstree.root.right.payload
        18
        >>> print(bstree.root)
                19
            18
                    17
                15
                    13
        12
                9
            5
                2
        <BLANKLINE>
        """

        if self.root is None:
            self.root = Node(payload)
            return

        previous_node = None
        node = self.root
        while node is not None:
            previous_node = node
            if payload < node.payload:
                node = node.left
            else:
                node = node.right
        if previous_node is None:
            self.root = Node(payload)
        elif payload < previous_node.payload:
            previous_node.left = Node(payload, parent=previous_node)
        else:
            previous_node.right = Node(payload, parent=previous_node)

        return

        # Recursive
        # if payload < self.payload:
        #     if self.left is None:
        #         self.left = Node(payload, parent=self)
        #     else:
        #         self.left.insert(payload)
        # else:
        #     if self.right is None:
        #         self.right = Node(payload, parent=self)
        #     else:
        #         self.right.insert(payload)

    def transplant(self, unode, vnode):
        """ Used by the delete method"""

        if unode.parent is None:
            self.root = vnode
        elif unode == unode.parent.left:
            unode.parent.left = vnode
        else:
            unode.parent.right = vnode
        if vnode:
            vnode.parent = unode.parent

    def delete(self, payload):
        """ Delete a node

        >>> bstree = BinaryTree(12)
        >>> for i in [5, 18, 2, 9, 15, 19, 13, 17]:
        ...     bstree.insert(i)
        >>> print(bstree.root)
                19
            18
                    17
                15
                    13
        12
                9
            5
                2
        <BLANKLINE>
        >>> bstree.delete(13) ; print(bstree.root)
                19
            18
                    17
                15
        12
                9
            5
                2
        <BLANKLINE>
        >>> bstree.delete(15) ; print(bstree.root)
                19
            18
                17
        12
                9
            5
                2
        <BLANKLINE>
        >>> bstree.delete(19) ; bstree.delete(18) ; print(bstree.root)
            17
        12
                9
            5
                2
        <BLANKLINE>
        >>> bstree.delete(5) ; print(bstree.root)
            17
        12
            9
                2
        <BLANKLINE>
        >>> bstree.delete(12) ; print(bstree.root)
        17
            9
                2
        <BLANKLINE>
        >>> bstree.delete(17) ; print(bstree.root)
        9
            2
        <BLANKLINE>
        """
        node = self.root.search(payload) if type(payload) is not Node else payload
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            successor = node.right.minimum()
            if successor.parent != node:
                self.transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self.transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
