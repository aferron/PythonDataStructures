# Binary Search Tree 

import random
random.seed()

class Node:
    def __init__(self):
        self.data = random.randint(1, 100)
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def build(self):
        nodes = random.randint(0, 10)
        inserted = 0
        for x in range (0, nodes):
            insertable = Node()
            inserted += self.insert(insertable)
        return inserted

    def insert(self, insertable):
        if self.root is None:
            self.root = insertable
        self._insert(self.root, insertable)
        return 1;

    def _insert(self, root, insertable):
        if root is None:
            root = insertable
            return 1
        if root.data < insertable.data:
            return self._insert(root.right, insertable)
        return self._insert(root.left, insertable)

    def display(self):
        return self.display_all(self.root)

    def display_all(self, root):
        if root is None:
            return 0
        self.display_all(root.left)
        print(root.data)
        return 1 + self.display_all(root.right)

tree = BST()
print ("Number of nodes in the tree is ", tree.build())
#print ("Root's data is ", tree.root.data)
print ("Number of nodes displayed is ", tree.display())
    
