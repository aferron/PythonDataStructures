# Stack implementation
# Amila Ferron
# CS300
# April 14, 2020

# Implements a flexible array for a stack -- a linked list of arrays



import random

# The size of each array
SIZE = 3

# The maximum value for the numbers added to the stack for testing
MAX_VALUE = 37

# The maximum number of entries that will be added to the stack for testing
MAX_ENTRIES = 23



# Array class has a list and a pointer to the next array.
class Array:



    # Creates a list, sets top to 0, and the next pointer to none
    def __init__(self):
        self.data = []
        self.top = 0
        self.next = None 



    # Appends to the list if the list has not reached maximum size
    # returns 1 if successfully added, None if not
    def push(self, value):
        if self.top >= SIZE:
            return None
        self.data.append(value)
        self.top += 1
        return 1



    # Removes the last data item added, and returns the value of that item
    def pop(self):
        if self.top == 0:
            return None 
        if self.top > SIZE:
            return None 
        self.top -= 1
        popped = self.data.pop()
        return popped 



    # Returns the value of the last item added
    def peek(self):
        if self.top == 0:
            return None
        if self.top > SIZE:
            return None
        return self.data[self.top - 1]



    # Removes all values in the list
    # Returns 1
    def remove_all(self):
        for i in self.data:
            self.data.pop()
        self.top = 0
        return 1



    # Displays all values in the list
    def display(self):
        for i in range(0, self.top):
            print(self.data[i], " ")






# Stack class is a linked list of arrays.
# When an array is at maximum size, a new array is added to the list.
class Stack:



    # Sets head to none
    def __init__(self):
        self.head = None



    # Adds data to the stack, calling a recursive function to add
    # to the end of the stack. It would be more efficient to add
    # at head instead of at the end of the linked list
    # Returns 1 if successful, 0 if not
    def push(self, value):
        if self.head is None:
            self.head = Array()
        if self.head.push(value) is None:
            add = Array()
            add.next = self.head
            self.head = add
            return self.head.push(value)
        return 1



    # Removes the last value added to the stack, returning the value
    def pop(self):
        if self.head is None:
            return None
        popped = self.head.pop()
        if self.head.peek() is None:
            remove = self.head
            self.head = self.head.next
        return popped
        #popped = list()
        #self.head = self._pop(self.head, popped)
        #return popped[0]



    # Recursively traverses to the end of the list to remove the last 
    # value added. Appends the value to popped (a list).
    # Returns head.
    def _pop(self, head, popped):
        if head is None:
            return None
        if head.next is None: 
            popped.append(head.pop())
            if head.top == 0:
                return None
            return head
        head.next = self._pop(head.next, popped)
        return head 



    # Gets the last value added
    def peek(self):
        if self.head is None:
            return None
        return self.head.peek()
        #return self._peek(self.head)



    # Recursively traverses to get the last value added
    def _peek(self, head):
        if head is None:
            return None
        if head.next is None:
            return head.peek()
        return self._peek(head.next)



    # Removes all values in the stack by setting head to None
    def remove_all(self):
        if self.head is not None:
            self.head = None



    # Displays all values in the stack, returning nothing
    def display(self):
        if self.head is not None:
            self._display(self.head)
        print()


    # Recursively traverses the list to display all values in the stack
    # Returns nothing.
    def _display(self, head):
        if head is None:
            return
        self._display(head.next)
        head.display()

    # Randomly get the size of the stack and push random values onto it
    def random_create(self):
        size = random.randint(1, MAX_ENTRIES)
        for i in range(0, size): 
            value = random.randint(1, MAX_VALUE)
            self.push(value)



    def test(self):

        # Seed the random number generator
        random.seed()

        # Create a class instance
        info = Stack()

        # Test peek with no data in stack:
        print("Peeking: ", info.peek())

        # Test random create and display
        info.random_create()
        print("The stack: ")
        info.display()

        # Test peek
        print("Peeking: ", info.peek())

        # Test pop
        print("Popping:")
        pop_times = random.randint(1, 5)
        for i in range(0, pop_times): 
            print(info.pop())
        print("The stack: ")
        info.display()

        # Test peek
        print("Peeking: ", info.peek())


        # Let the user experience push, peek, and pop:
        push_value = int(input("Enter a number to push onto the stack: "))
        info.push(push_value)
        print("The stack is now: ")
        info.display()
        print("Peeking: ", info.peek())
        print("Popping, the value returned is: ", info.pop())


        # Test remove all
        info.remove_all()
        print("The stack after remove all: ")
        info.display()
