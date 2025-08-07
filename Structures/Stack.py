from collections import stack

class Stack:
    list = []

    def __init__(self):
        pass

    def append(self, value):
        self.list.append(value)
        return 0
    
    def pop(self):
        self.list.pop()
        return 0

    def peek(self):
        return self.list[-1]

    def isempty(self):
        return (len(self.list) == 0)





test = Stack()

test.append(8)

print(test.peek())

test.append(7)

print(test.peek())

test.pop()
test.pop()

print(test.isempty())