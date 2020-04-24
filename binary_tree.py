# binary tree

from queue_2_stacks import Queue

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

    def left_is_full(self):
        if self.left is None:
            return 0
        return 1

    def right_is_full(self):
        if self.right is None:
            return 0
        return 1

    def add_at_left(self, value):
        self.left = Node(value)
        return 1

    def add_at_right(self, value):
        self.right = Node(value)
        return 1
    
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return 1

        Queue.enqueue(self.root, value)
        added = 0

        while added == 0:
            current = Queue.dequeue()
            if current.left_is_full == 0:
                current.add_at_left(value)
                added = 1
            else:
                Queue.enqueue(current.left)
            if added == 0 and current.right_is_full == 0:
                current.add_at_right(value)
                added = 1
            elif added == 0:
                Queue.enqueue(current.right)

    def display(self):
        return self._display(self.root)

    def _display(self, root):
        if root is None:
            return 0
        displayed = self._display(root.left)
        print(root.data, " ")
        return displayed + 1 + self._display(root.right)

    def prompt_for_input(self):
        done = 0
        while 0 == done:
            try:
                value = int(input("value: "))
            except ValueError:
                print("Enter only integers")
            else:
                done = 1
        return value


    def test(self):
        done = 0
        count  = 0        
        print("Enter integer values to add, negative value to stop")

        while 0 == done:
            add = self.prompt_for_input()
            if add >= 0:
                self.insert(add)
            else:
                done = 1
            count += 1

        print("There are ", count, " items in the list:")
        self.display()
        print()



measurements = BinaryTree()
measurements.test()

            

        



        
        
