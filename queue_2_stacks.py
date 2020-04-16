# Queue implemented with two stacks

from stack import Stack


primary = Stack()


class Queue:
    

    def __init__(self):
        self.primary = Stack()
        self.secondary = Stack()



    def create(self):
        self.primary.random_create()



    def enqueue(self, value):
        self.primary.push(value)



    def dequeue(self):
        
        #while popped = self.primary.pop() is not None:
        popped = self.primary.pop()
        while popped is not None:
            self.secondary.push(popped)
            popped = self.primary.pop()
        dequeued = self.secondary.pop()
        popped = self.secondary.pop()
        while popped is not None:
            self.primary.push(popped)
            popped = self.secondary.pop()
        return dequeued



    def peek(self):
        popped = self.primary.pop()
        while popped is not None:
            self.secondary.push(popped)
            popped = self.primary.pop()
        peeked = popped = self.secondary.pop()
        while popped is not None:
            self.primary.push(popped)
            popped = self.secondary.pop()
        return peeked 

    

    def display(self):
        self.primary.display() 



    def test(self):
        self.create() 
        print("The original list: ")
        self.display()
        print("Peeked value is: ", self.peek())
        print("Dequeued value is: ", self.dequeue())
        print("The new list: ")
        self.display()
        print("Peeked value is: ", self.peek())
        print("Enqueue 7: ")
        self.enqueue(7)
        print("The new list: ")
        self.display()
        print("Peeked value is: ", self.peek())
        print("Dequeued value is: ", self.dequeue())
        print("The new list: ")
        self.display()
        print("Peeked value is: ", self.peek())
        print("Enqueue 14: ")
        self.enqueue(14)
        print("The new list: ")
        self.display()
        print("Peeked value is: ", self.peek())

        


data = Queue()        
data.test()





