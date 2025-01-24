class Stack: 

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0 
    
stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop(), end=" ")
    
stack = Stack()
for item in ("Hello,", "world!"):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop())