class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, *data):
        self.root = None
        for value in data:
            self.insert(value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            temp = self.root
            while True:
                if value < temp.value:
                    if temp.left is None:
                        temp.left = Node(value)
                        break
                    else:
                        temp = temp.left
                elif value > temp.value:
                    if temp.right is None:
                        temp.right = Node(value)
                        break
                    else:
                        temp = temp.right
                else:
                    break

    def contains(self, value):
        if self.root is None:
            return False
        else:
            temp = self.root
            while True:
                if value == temp.value:
                    return True
                elif value < temp.value:
                    if temp.left is None:
                        return False
                    else:
                        temp = temp.left
                elif value > temp.value:
                    if temp.right is None:
                        return False
                    else:
                        temp = temp.right
                    

    def print(self):
        temp = self.root



if __name__ == '__main__':
    tree = BinarySearchTree(1, 2, 3, 4, 5, 6, 7)
print(    tree.contains(9))