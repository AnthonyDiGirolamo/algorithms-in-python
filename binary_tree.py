
class Node:
    """Binary Tree Node class

    >>> btree = Node('5')
    >>> for i in ['4', '6', 'r', 'v', 'a', 'x']:
    ...     btree.insert(i)
    ...
    >>> btree.print_in_order()
    4
    5
    6
    a
    r
    v
    x
    >>> [node.payload for node in btree.in_order_walk()]
    ['4', '5', '6', 'a', 'r', 'v', 'x']
    >>> btree.search('x')
    'x'
    >>> btree.search('z')
    """

    def __init__(self, payload, left=None, right=None, parent=None):
        self.payload = payload
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return repr(self.payload)

    def insert(self, payload):
        node = self
        previous_node = None
        while node is not None:
            previous_node = node
            if payload < node.payload:
                node = node.left
            else:
                node = node.right
        if previous_node is None:
            self = Node(payload)
        if payload < previous_node.payload:
            previous_node.left = Node(payload)
        else:
            previous_node.right = Node(payload)
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

    def in_order_walk(self):
        if self.left:
            for node in self.left.in_order_walk():
                yield node
        yield self
        if self.right:
            for node in self.right.in_order_walk():
                yield node

class BinaryTree:

    def __init__(self, root_payload=None):
        self.root = Node(root_payload)

    def insert(self, payload):
        self.root.insert(payload)

    def delete(self):
        pass

    def __repr__(self):
        return repr([i for i in self])

if __name__ == "__main__":
    import doctest
    doctest.testmod()

