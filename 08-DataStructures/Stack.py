class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack)==0
    
    def __str__(self):
        return str(self.stack) 

stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
print(stack1)
stack1.pop()
stack1.pop()
stack1.pop()
print(stack1)
