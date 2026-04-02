import pytest
from DSA.DLL import *

def test_reverse():
    doubly = DoublyLinkedList(1, 2, 3, 4, 5)
    doubly.reverse()
    assert doubly.show() == [5, 4, 3, 2, 1]