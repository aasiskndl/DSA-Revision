"""
Is a complex type of linked list in which each node contains a data element and two pointers.
One points to the next node in te sequence, while the other points to the previous node.

each node contains:
- data
- pointer to next node
- pointer to previous node
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLL:
    def __init__(self):
        self.head = None
        
    # insert at begining
    def insert_front(self, data):
        new_node = Node(data)
            
        if self.head is not None:
                self.head.prev = new_node
                new_node.next = self.head
                
        self.head = new_node
            
        # insert at end
    def insert_end(self, data):
            new_node = Node(data)
            
            if self.head is None:
                self.head = new_node
                return 
            
            temp = self.head
            while temp.next:
                temp = temp.next
            
            temp.next = new_node
            new_node.prev = temp
            
        # delete a node by value
    def delete(self, key):
        temp = self.head
            
        while temp:
            if temp.data == key:
                    # detecting head
                if temp.prev is None:
                    self.head = temp.next
                        
                if self.head:
                        self.head.prev = None
                else:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return 
            temp = temp.next
        
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end="<=>")
            temp = temp.next
        print("None")
            
        # display ackward
    def display_backward(self):
        temp = self.head
            
        if temp is None:
            return 
            
            # go to the last node
        while temp.next:
            temp = temp.next
                
            # traverse backward
        while temp:
            print(temp.data, end="<=>")
            temp = temp.prev
        print("None")
            
dll = DoublyLL()

dll.insert_front(2)
dll.insert_front(1)
dll.insert_end(3)
dll.insert_end(4)

dll.display_forward()

dll.delete(3)

dll.display_forward()
dll.display_backward()    
                