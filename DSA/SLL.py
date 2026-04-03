
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
            self.get(index).data = value
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
            return None
        else:
            current = self.head
            content = []
            while current.next is not None:
                content.append(current.data)
                current = current.next
            content.append(self.tail.data)
            return content

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
        if self.head is None:
            return self
        if self.head is self.tail:
            return self
        old_head = self.head
        old_tail = self.tail
        curr = self.head
        prev = None
        while curr is not None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        self.head = old_tail
        self.tail = old_head
        self.tail.next = None
        return self

    def middle(self):
        if self.head is None:
            return None
        if self.head is self.tail:
            return self.head

        else:
            mid = self.head
            runna = self.head
            while runna is not None and runna.next is not None:
                mid = mid.next
                runna = runna.next.next
            return mid
    def has_cycle(self):
        if self.head is None:
            return False
        if self.head is self.tail:
            return False
        else:
            slow = fast = self.head
            while fast and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True

        return False

def merge_lists(list1, list2):
    list1Node = list1.head
    list2Node = list2.head
    new = SinglyLinkedList()
    while list1Node and list2Node:
        if list1Node.data < list2Node.data:
            new.append(list1Node.data)
            list1Node = list1Node.next
        else:
            new.append(list2Node.data)
            list2Node = list2Node.next
    while list1Node:
        new.append(list1Node.data)
        list1Node = list1Node.next
    while list2Node:
        new.append(list2Node.data)
        list2Node = list2Node.next
    return new
        
if __name__ == "__main__":
    linked = SinglyLinkedList(1,2,3,4,5)
    print(linked.show())
    linked.reverse()
    print(linked.show())
