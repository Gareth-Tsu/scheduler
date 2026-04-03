class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, *values):
        self.top = None
        self.height = 0
        for value in values:
            self.push(value)

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return self

    def pop(self):
        if self.top is None:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp
    
    def show(self):
        if self.top is None:
            print("empty stack")
        else:
            content = []
            temp = self.top
            while temp is not None:
                content.append(temp.value)
                temp = temp.next
    
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
            self.length += 1
            return self
        else:
            new_node.next = self.last
            self.last = new_node
            self.length += 1
            return self
    def dequeue(self):
        if self.last is None:
            return None
        else:
            temp = self.last
            self.last = self.last.next
            self.length -= 1
            return temp
    def show(self):
        if self.last is None:
            print("empty queue")
            return None
        else:
            temp = self.last
            content = []
            while temp is not None:
                content.append(temp.value)
                temp = temp.next
            return content

#This function fails the tests, and I am not sure why
def is_valid(string):
    stack = Stack()
    matches = {")": "(", "]": "[", "}": "{"}
    for char in string:
        if char in "({[":
            stack.push(char)
        elif char in matches:
            if stack.height == 0 or stack.top.value != matches[char]:
                return False
            stack.pop()
    return stack.height == 0