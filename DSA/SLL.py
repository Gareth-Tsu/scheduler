
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return f"{self.data}"
    def jump(self):
        return self.next


class SinglyLinkedList:
    def __init__(self, *data):
        self.head = None
        self.tail = None
        self.count = 0
        for value in data:
            self.append(value)
    
    def append(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
            self.count += 1
            return self
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.count += 1
            return self
    
    def prepend(self, data):
        if self.head is None:
            NewNode = Node(data)
            self.head = NewNode
            self.tail = NewNode
            self.count += 1
            return self
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.count += 1
            return self
        
    
    def get(self, index: int):
        if index < 0 or index >= self.count:
            return None
        else:
            current = self.head
            count = 0
            while count < index:
                current = current.next
                count += 1
            return current

            
    def set(self, index, value):
        if index < 0 or index >= self.count:
            return None
        else:
            current = self.head
            count = 0
            while count < index:
                current = current.next
                count += 1
            current.data = value
            return self

    def insert(self, data, index):
        new_node = Node(data)
        if index < 0 or index >= self.count:
            return None
        else:
            prev = self.head
            curr = self.head.next
            count = 1
            while count < index:
                prev = curr
                curr = curr.next
                count += 1
            prev.next = new_node
            new_node.next = curr
            self.count += 1
            return self

    def pop(self):
        if not self.head:
            return None
        if self.head is self.tail:       # single element
            value = self.head.data
            self.head = self.tail = None
            self.count = 0
            return value

        prev = self.head
        curr = self.head.next
        while curr is not self.tail:
            prev = curr
            curr = curr.next

        value = self.tail.data
        self.tail = prev
        self.tail.next = None
        self.count -= 1
        return value



    def show(self):
        if self.head is None:
            print("Empty List")
        else:
            current = self.head
            content = []
            while current.next is not None:
                content.append(current.data)
                current = current.next
            content.append(self.tail.data)
            print(content)

    def first_pop(self):
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        return value
    
    def remove(self, index):
        if index < 0 or index >= self.count or self.head is None:
            return None
        if index == 0:
            removed = self.head
            self.head = removed.next
            if removed is self.tail:
                self.tail = None
        else:
            prev = self.get(index - 1)
            removed = prev.next
            prev.next = removed.next
            if removed is self.tail:
                self.tail = prev
        removed.next = None
        self.count -= 1
        return self
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = self.head
        for n in range(self.count):
            pass


        

linked = SinglyLinkedList(1, 4, 9, 16, 25)
linked.insert(10, 3)
linked.insert(1, 0)
linked.remove(0)
linked.show()
