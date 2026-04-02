import pytest
from DSA.SLL import *

linked = SinglyLinkedList(1,2,3,4,5,6,7,8,9,10)

def test_reverse_linked_list():
    linked.reverse()
    assert linked.show() == [10,9,8,7,6,5,4,3,2,1]