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
    
    def print(self):
        if self.top is None:
            print("empty stack")
        else:
            temp = self.top
            while temp is not None:
                print(temp.value)
                temp = temp.next
    
class Queue:
    def __init__(self):
        self.top = None
        self.height = 0
Empty = Stack()
Empty.push(1)
Empty.print()
