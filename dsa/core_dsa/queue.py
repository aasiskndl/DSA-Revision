# queue is also a linear data structure that follows first in, first out principle
# the first element inserted is the first one to be removed
# just like an real queue in ticket counter

class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"
    
    def display(self):
        print(self.items)
        
#performing some operations 
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

print(q.dequeue())
print(q.peek())
q.display()