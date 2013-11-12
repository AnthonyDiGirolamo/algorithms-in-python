
class Node:

    def __init__(self, payload, left=None, right=None, parent=None):
        self.payload = payload
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return repr(self.payload)

    def insert(self, payload):
        if payload < self.payload:
            if self.left is None:
                self.left = Node(payload, parent=self)
            else:
                self.left.insert(payload)
        else:
            if self.right is None:
                self.right = Node(payload, parent=self)
            else:
                self.right.insert(payload)

    def print_breadth_first(self):
        if self.left:
            self.left.print_breadth_first()
        print(self.payload)
        if self.right:
            self.right.print_breadth_first()

class BinaryTree:
    """BinaryTree class

    >>> btree = BinaryTree('a')
    >>> btree.insert('b')
    >>> btree.insert('A')
    >>> btree.insert('c')
    >>> btree.root.print_breadth_first()
    """

    def __init__(self, root_payload=None):
        self.root = Node(root_payload)

    def insert(self, payload):
        self.root.insert(payload)

    def delete(self):
        pass

    def __repr__(self):
        return repr([i for i in self])

    # def __iter__(self):
    #     self.current_node = None
    #     return self

    # def __next__(self):
    #     if self.current_node == None:
    #         self.current_node = self.root
    #     elif self.current_node.left != None:
    #         self.current_node = self.current_node.left
    #     elif self.current_node.right != None:
    #         self.current_node = self.current_node.right
    #     else:
    #         raise StopIteration
    #     return self.current_node.payload

    def __len__(self):
        return self.size

    # def __getitem__(self, index):
    #     return self.todo_items[index]

if __name__ == "__main__":
    import doctest
    doctest.testmod()

