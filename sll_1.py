# Singularly linked list


import random
random.seed()
class Node:
    def __init__(self):
        #self.data = 5
        self.data = random.randint(0, 100)
        self.next = None

    def equality(self, comparable):
        print("In equality function, comparable is:")
        print(comparable)
        print("In equality function, self.data is:")
        print(self.data)
        if comparable == self.data:
            return True
        return False
        

class SLL:
    def __init__(self):
        self.head = None

    def compare(self):
        self.head = Node()
        print(self.head.equality(5))

    def custom_build(self):
        self.head = Node()
        current = self.head
        current.next = Node()
        current = current.next
        current.next = Node()
        current = current.next
        current.next = Node()
        current = current.next
        current.next = Node()
        return self
    def display(self):
        return self._display(self.head)

    def _display(self, head):
        if head is None:
            return 0
        print(head.data)
        return 1 + self._display(head.next)

    def remove_all(self):
        self.head = None


    def build(self):
        nodes = 3
        self.head = Node()
        self._build(self.head, 0, nodes)
        return self

    def _build(self, head, count, max_nodes):
        if count is max_nodes:
            return head
        head.next = Node()
        self._build(head.next, count + 1, max_nodes)
        return head

    def set_head(self):
        self.head = self._set_head(self.head)
        print("The data in head is: " )
        print(self.head.data)
        return self.head

    def _set_head(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        return self._set_head(head.next)


    def remove(self, removable):
        self.head = self._remove(self.head, removable)
        return 


    def _remove(self, head, removable):
        if head is None:
            return None
        print("head.data:")
        print(head.data)
        print("removable")
        print(removable)
        print (head.data == removable)
        print (head.equality(removable))
        if head.data == removable:
            print("Match found")
            return head.next
        if head.next is None:
            print("reached end of list, data is: ")
            print(head.data)
            return head
        if head.next.data == removable:
            print("Match found at next node")
            head.next = head.next.next
            return head
        head.next = self._remove(head.next, removable)
        print("remove function at")
        print(head.data)
        return head

test_list = SLL()
test_list.compare()
head = Node()
print(head.equality(5))
print(head.data + 20)
x = 5
print(head.data + x)
print(head.equality(x))

list_A = SLL()
list_A.build()
print("This is the list:")
list_A.display()


removable = int(input("Which number would you like to remove?"))
list_A.remove(removable)
print("This is the list after remove:")
list_A.display()

list_A.set_head()

list_A.remove_all()
print("This is the list after remove all:")
list_A.display()

print()


