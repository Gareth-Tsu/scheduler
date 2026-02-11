class MaxHeap:
    def __init__(self):
        self.heap = []

    def left_child(self, index):
        return index * 2 + 1

    def right_child(self, index):
        return index * 2 + 2

    def parent(self, index):
        return (index - 1) // 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, *values):
        for value in values:
            self.heap.append(value)
            i = len(self.heap) - 1  # <-- track position of the inserted value

            # bubble up
            while i > 0:
                p = self.parent(i)
                if self.heap[i] <= self.heap[p]:
                    break
                self.swap(i, p)
                i = p

    def sink(self):
        i = 0
        if len(self.heap) > 1:
            while True:
                rc = self.right_child(i) # Index of the right child
                lc = self.left_child(i)  # Index of the lift child
                if lc >= len(self.heap):
                    break
                if rc < len(self.heap):
                    if self.heap[i] >= self.heap[lc] and self.heap[i] >= self.heap[rc]:
                        break
                    else:
                        child = rc if self.heap[rc] > self.heap[lc] else lc
                        self.swap(i, child)
                        i = child
                else:
                    if self.heap[i] >= self.heap[lc]:
                        break
                    else:
                        self.swap(i, lc)
                        i = lc

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        else:
            value = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.swap(0, (len(self.heap) - 1))
            self.sink()
            return value




    def __str__(self):
        return str(self.heap)


new = MaxHeap()
new.insert(2, 3, 4, 8, 9)
new.insert(1, 6, 12, 65)
print(new)
