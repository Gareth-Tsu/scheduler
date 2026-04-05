import pytest
from DSA.BST import *

def test_invert():
    # Normal tree
    tree = BinarySearchTree(4, 2, 7, 1, 3, 6, 9)
    tree.inverse()
    assert tree.root.value == 4,          "Failed: root unchanged"
    assert tree.root.left.value == 7,     "Failed: left should be 7"
    assert tree.root.right.value == 2,    "Failed: right should be 2"
    assert tree.root.left.left.value == 9,  "Failed: left.left should be 9"
    assert tree.root.left.right.value == 6, "Failed: left.right should be 6"
    assert tree.root.right.left.value == 3, "Failed: right.left should be 3"
    assert tree.root.right.right.value == 1,"Failed: right.right should be 1"

    # Single node
    tree2 = BinarySearchTree(1)
    tree2.inverse()
    assert tree2.root.value == 1, "Failed: single node"

    # Empty tree
    tree3 = BinarySearchTree()
    assert tree3.inverse() is None, "Failed: empty tree"

    print("All invert tests passed!")