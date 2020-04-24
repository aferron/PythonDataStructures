# Singularly linked list
# Amila Ferron
# April 7, 2020
# Includes functions to create a list automatically, or to create a custom list, 
# functions to display, remove all, remove one, find, and increment (update) the
# list by an entered number.

import pdb
import random
random.seed()
class Node:

    # Node constructor takes a value as an argument
    def __init__(self, init_value):
        self.data = init_value
        self.next = None

    # Checks for equality
    def equality(self, comparable):
        if comparable == self.data:
            return True
        return False
        

class SLL:

    # SLL constructor just sets head to None
    def __init__(self):
        self.head = None



    # Display function calls the recursive display function
    # It returns the number of items displayed
    def display(self):
        return self._display(self.head)



    # Resursive display function returns the number of items displayed
    def _display(self, head):
        if head is None:
            return 0
        print(head.data)
        return 1 + self._display(head.next)



    # Displays a list with the list head given as an argument
    def disp(self, head):
        if head is None:
            print()
            return
        print(head.data, " ", end='')
        return self.disp(head.next)
        


    # Remove all is simple with garbage collection
    def remove_all(self):
        self.head = None



    # Build function creates a random number of nodes between 0 and 10
    # Each node is given a random number as its data value
    def build(self):
        nodes = random.randint(0, 10)
        self.head = Node(random.randint(0, 100))
        self._build(self.head, 0, nodes)
        return self



    # Recursive build function assigns a random number to each node
    def _build(self, head, count, max_nodes):
        if count is max_nodes:
            return head
        head.next = Node(random.randint(0, 100))
        self._build(head.next, count + 1, max_nodes)
        return head



    # Remove function calls the recursive remove function
    def remove(self, removable):
        self.head = self._remove(self.head, removable)
        return 



    # Recursive remove function unlinks a node if it contains the same 
    # data as what was entered by the user
    def _remove(self, head, removable):
        if head is None:
            return None
        if head.data == removable:
            return head.next
        head.next = self._remove(head.next, removable)
        return head

    # Prompt function to interface with the user and error check
    def prompt_for_remove(self):
        try:
            removable = int(input("Which number would you like to remove?"))
        except ValueError:
            print("That is not a number. Remove can't happen.\n")
        else:
            list_A.remove(removable)
            print("This is the list after remove:")
            list_A.display()



    # Insert at end function adds a node to the end of the list
    # It could make more sense to add to the start of the list
    def insert_at_end(self, insertable):
        self.head = self._insert(self.head, insertable)



    # Resursive insert at end function traverses to the end and adds a node there
    # with the value entered by the user
    def _insert_at_end(self, head, insertable):
        if head is None:
            head = Node(insertable)
            return head
        head.next = self._insert(head.next, insertable)
        return head



    # Prompt function interfaces with the user to get a value to insert, 
    # checks for errors in the value entered, and calls the insert function.
    def prompt_for_insert(self):
        valid = 1
        try:
            insertable = int(input("Create a custom list. Enter positive numbers to continue, negative to end."))
        except ValueError:
            print("Need an integer, cannot insert")
            return
        while insertable >= 0:
            if valid:
                self.insert(insertable)
                print("This is the list:")
                self.display()
            valid = 1
            try:
                insertable = int(input("Enter another value:"))
            except ValueError:
                print("Need an integer, cannot insert")
                valid = 0
        self.display()



    # Find function calls the resursive find function
    def find(self, search_value):
        return self._find(self.head, search_value)



    # Recursive find function traverses the list, returning 1 if the value
    # entered by the user was found and 0 if not
    def _find(self, head, search_value):
        if head is None:
            return 0
        if head.data == search_value:
            return 1
        return self._find(head.next, search_value)



    # Prompt function interfaces with the user to get a value to find, 
    # checks the value entered to be sure it is an int, and calls the find function
    def prompt_for_find(self):
        try:
            value = int(input("Enter a value to find in the list:"))
        except ValueError:
            print("Need a number, that value cannot be found.")
        else:
            found = list_A.find(value)
            print("The value ", value, "was", end='')
            if found == 0:
                print(" not", end='')
            print(" found.")



    # Increment function calls the recursive increment function
    def increment(self, incrementer):
        head = self._increment(self.head, incrementer)



    # Recursive increment function traverses the list, adding the value entered by
    # the user to the data value in each node
    def _increment(self, head, incrementer):
        if head is None:
            return head
        head.data += incrementer
        head.next = self._increment(head.next, incrementer)
        return head



    # Prompt function interfaces with the user to get a value to increment the list by,
    # performs error checking, calls the increment function, and displays the list 
    def prompt_for_increment(self):
        try:
            incrementer = int(input("Enter a value to increment the list by:"))
        except ValueError:
            print("Invalid value entered, please only enter numbers")
        list_A.increment(incrementer)
        print("This is the list after incrementing:")
        list_A.display()



    # Push adds a node at the head of the list, with data input by the user.
    def push(self, pushable):
        temp = self.head
        self.head = Node(pushable)
        self.head.next = temp



    # Prompt for push interfaces with the user to get a value to push.
    def prompt_for_push(self):
        try:
            pushable = int(input("Enter an integer value to add to the list: "))
        except ValueError:
            print("Must be an integer, cannot add to the list.")
            return
        self.push(pushable)
        print("This is the list:")
        list_A.display()
        print()



    # Pop removes the last node from the list
    def pop(self):
        self.head = self._pop(self.head)
        print("This is the list after removing: ")
        self.display()
        


    # Recursive pop function traverses to the end of the list and removes the last node
    def _pop(self, head):
        if head is None:
            return head
        if head.next is None:
            return None
        head.next = self._pop(head.next)
        return head



    def sort(self):
        array_list = []
        self.make_array(self.head, array_list, 0)
        length = len(array_list)
        array_list = self._sort(array_list, 0, length - 1)
        for i in range (0, length - 1):
            array_list[i].next = array_list[i + 1]
        print("The sorted list: ")
        self.display()
        print()



    def make_array(self, head, array, i):
        if head is None:
            return
        array.append(head)
        self.make_array(head.next, array, i + 1)
        head.next = None



    # Recursive merge sort function
    def _sort(self, array, lower, upper):
        #print("lower: ", lower, " upper: ", upper)
        if lower >= upper:
            #print (self.list[lower], ' ', end='')
            mini_list = [array[lower]]
            return mini_list
        mid = lower + int((upper - lower)/2)
        left = self._sort(array, lower, mid)
        right = self._sort(array, mid + 1, upper)

        if left is None:
            return right
        if right is None:
            return left

        # Merge lists:
        left_length = len(left)
        right_length = len(right)
        merged = list() 
        i = 0
        j = 0
        while i < left_length or j < right_length:
            if i == left_length:
                merged.append(right[j])
                j += 1
            elif j == right_length:
                merged.append(left[i])
                i += 1
            elif left[i].data < right[j].data:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        return merged


    # Recursive sort function continually divides the list in half, 
    # creating new, merged, sorted lists as the stack unwinds
    #def _sort(self, origin, head, traverses, target):
    #    if head is None:
    #        return head
    #    if 0 == target:
    #        return head
    #    if traverses == target:
    #        target = int(target / 2)
    #        if target != 0:
    #            left = self._sort(origin, origin, 1, target)
    #            right = self._sort(head, head, 1, target)
    #            print("left: ", left.data, "  right: ", right.data)
    #        else:
    #            print("head: ", head.data)
    #        return head
    #    traverses = int(traverses + 1)
    #    head.next = self._sort(origin, head.next, traverses, target) 


    # Recursive function to get the node pointer at the entered location in the list
    # Return value is a node pointer
    def _get_mid(self, head, location, target):
        if head is None:
            return None
        if location == target:
            return head
        return self._get_mid(head.next, location + 1, target)


    # Length of the list is returned
    def len(self, head):
        if head is None:
            return 0
        return 1 + self.len(head.next)



        


# testing the functions of the SLL:
list_A = SLL()

list_A.build()
print("This is the automatically created list:")
list_A.display()
print()

#pdb.set_trace()
list_A.sort()

#list_A.prompt_for_push()

#list_A.pop()

#list_A.remove_all()
#print("This is the list after remove all:")
#list_A.display()
#print()

#list_A.prompt_for_insert()

#list_A.prompt_for_remove()

#list_A.prompt_for_find()

#list_A.prompt_for_increment()

#print()


