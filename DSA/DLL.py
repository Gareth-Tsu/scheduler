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

    def show(self):
        temp = self.head
        content = []
        if temp is None:
            print("Empty list")
        else:
            while temp is not None:
                content.append(temp.value)
                temp = temp.next
        return content

    def reverse(self):
        if self.head is None:
            return None
        if self.head is self.tail:
            return None
        else:
            old_head = self.head
            old_tail = self.tail
            curr = old_head
            prev = None
            while curr is not None:
                curr.prev = curr.next
                curr.next = prev
                prev = curr
                curr = curr.prev
            self.head = old_tail
            self.tail = old_head
            return self



