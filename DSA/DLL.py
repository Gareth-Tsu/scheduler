"""
Learning to create and work with doubly linked lists
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, *data):
        self.head = None
        self.tail = None
        self.length = 0
        for data in data:
            self.append(data)

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            new_node.prev = prev
            self.length += 1

    def print(self):
        temp = self.head
        content = []
        if temp is None:
            print("Empty list")
        else:
            while temp is not None:
                content.append(f"{temp.value}")
                temp = temp.next
        print(content)

if __name__ == "__main__":
    double = DoublyLinkedList(1,2,3,4,5,6,7)
    double.append(41)
    double.print()