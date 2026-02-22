'''
A circular queue is a linear data structure where: the last position is connected back to the first position, forming a circle.
It uses fixed-size array efficiently by reusing empty spaces.
we use: the idea of front -> points to first element
                    rear -> points to last element
'''

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
        
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear+1) % self.size == self.front
    
    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
            return
        
        if self.is_empty():
            self.front = 0 
        
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        
        value = self.queue[self.front]
        
        if self.front == self.rear:
            # only one element
            self.front = -1
            self.rear = -1
        else: 
            self.front = (self.front + 1) % self.size
        return value
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return 
        
        i = self.front
        while True:
            print(self.queue[i], end= " ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()
        
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)

cq.dequeue()    # removes 1
cq.dequeue()    # removes 2

cq.enqueue(5)
cq.enqueue(6)

cq.display()
