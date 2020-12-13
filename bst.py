# Binary Search Tree

from sys import getrefcount
import random
from queue import Queue
random.seed()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

class BST:
    def __init__(self):
        self.root = None

    def build(self):
        nodes = random.randint(1, 30)
        for x in range (0, nodes):
            insertable = TreeNode(random.randint(-(2**31), (2**31) - 1))
            self.root = self.insert(insertable)
        return nodes

    def insert(self, insertable):
        if self.root is None:
            self.root = insertable
            return self.root
        self.root = self._insert(self.root, insertable)
        return self.root;

    def _insert(self, root, insertable):
        if root is None:
            root = insertable
            return root
        if root.val < insertable.val:
            root.set_right(self._insert(root.right, insertable))
        else:
            root.set_left(self._insert(root.left, insertable))
        return root

    def display(self):
        displayed = self.display_all(self.root)
        print()
        return displayed

    def display_all(self, root):
        if root is None:
            return 0
        self.display_all(root.left)
        print(root.val, end =" ")
        return 1 + self.display_all(root.right)

    def display_pretty(self):
        if self.root is None:
            return 0
        return self._pretty(self.root)

    def _pretty(self, root):
        a = Queue()
        b = Queue()
        count = 0

        a.put(root)

        while a.empty() is False or b.empty() is False:
            while a.empty() is False:
                displayable = a.get()
                if displayable.left:
                    b.put(displayable.left)
                if displayable.right:
                    b.put(displayable.right)
                print(displayable.val, end =" ")
                count += 1

            print("\n")

            while b.empty() is False:
                displayable = b.get()
                if displayable.left:
                    a.put(displayable.left)
                if displayable.right:
                    a.put(displayable.right)
                print(displayable.val, end =" ")
                count += 1

            print("\n")
        return count

    def isValid(self):
        return self.isValidBST(self.root)

    def isValidBST(self, root):
        lastVisited = {"visited": None}
        return self._isValidBST(root, lastVisited)

    def _isValidBST(self, root, prev):
        if root is None:
            return True
        valid = self._isValidBST(root.left, prev)
        valid = valid and (prev["visited"] == None or prev["visited"] < root.val)
        prev["visited"] = root.val
        return valid and self._isValidBST(root.right, prev)






tree = BST()
print ("Number of nodes in the tree is ", tree.build())
#print ("Root's val is ", tree.root.val)
tree.display()
print ("Number of nodes displayed is ", tree.display_pretty())
if tree.isValid():
    print("Valid tree")
else:
    print("not valid")
