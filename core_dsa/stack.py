# stack is a linear data structure that uses last in first out principle
# the last element pushed is the one that is popped out at first


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty!"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty!"

    def display(self):
        print(self.items)


# eg
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print(stack.pop())
print(stack.peek())
stack.display()
