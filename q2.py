# Linked list as an array
# Amila Ferron
# April 9, 2020
# This file makes a linked list using an array. 
# New items are inserted at the end of the list.

import random
random.seed()

class list_as_array:
    def __init__(self):
        self.list = [0]
        self.top= 0
        # top points to the index where the next number should be inserted:

    def auto_create(self):
        self.list[0] = random.randint(0, 20)
        for i in range (0, 10):
            self.list.append(random.randint(0, 20))
        self.top = 10
        print("The initial list is: ")
        self.display()


    def create(self):
        valid = 1
        try:
            insertable = int(input("Enter positive integers to add to the list, negative to stop: "))
        except ValueError:
            print("List only numbers, cannot build list")
        while insertable >= 0:
            if valid == 1:
                if self.top == 0:
                    self.list[0] = insertable
                else:
                    self.list.append(insertable) 
                self.top += 1
                print("This is the list:")
            
            valid = 1
            try:
                insertable = int(input("Enter another number to add to the list:"))
            except ValueError:
                print("Enter only integers, try again:")
                valid = 0
        print("This is the completed list:")
        self.display()


    def display(self):
        length = len(self.list)
        for i in range (0, length):
            if self.list[i] is not None:
                print(self.list[i], end=' ')
        print("\n")

    # Removes all instances of a number passed in as an argument
    def remove(self, removable):
        removed = 0
        for i in range (0, self.top):
            if self.list[i] == removable:
                self.list[i] = None
                removed = 1
        return removed

    def prompt_for_remove(self):
        try:
            removable = int(input("Enter the number you would like to remove: "))
        except ValueError:
            print("Enter only integers, cannot remove.")
        if self.remove(removable):
            print("This is the list after removing: ")
            self.display()
        else:
            print("The number was not removed.")

    def find(self, search_value):
        found = 0
        print("self.top is ", self.top)
        print("length is ", len(self.list))
        for x in range(0, self.top):
            if self.list[x] == search_value:
                found = 1
                return found
        return found

    def prompt_for_find(self):
        try:
            search_value = int(input("Enter a integer value to find in the list: "))
        except ValueError:
            print("Cannot search for a non-integer")
        print("The value ", search_value, " was", end='')
        if not self.find(search_value, end=''):
            print(" not", end='')
        print(" found.")

    def update(self, incrementer):
        for i in range(0, self.top):
            if self.list[i] is not None:
                self.list[i] += incrementer

    def prompt_for_update(self):
        try:
            incrementer = int(input("Enter an integer amount to increment the list by: "))
        except ValueError:
            print("Entered value must be an integer. Cannot increment.")
        self.update(incrementer)
        print("This is the updated list: ")
        self.display()

    def sort(self):
        self.list = self._sort(0, self.top - 1)
        self.display()


    def _sort(self, lower, upper):
        #print("lower: ", lower, " upper: ", upper)
        if lower >= upper:
            #print (self.list[lower], ' ', end='')
            mini_list = [self.list[lower]]
            return mini_list
        mid = lower + int((upper - lower)/2)
        left = self._sort(lower, mid)
        right = self._sort(mid + 1, upper)


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
            elif left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        return merged

    def disp(self, displayable):
        length = len(displayable)
        for i in range(0, length):
            print(displayable[i], " ", end='')



            







my_list = list_as_array()

my_list.auto_create()

my_list.sort()
print("The sorted list: ")
my_list.display()

#my_list.prompt_for_find()

#my_list.prompt_for_remove()
#my_list.display()


#my_list.prompt_for_update()




