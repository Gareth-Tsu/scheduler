import pytest
from DSA.SLL import *

linked = SinglyLinkedList(1,2,3,4,5,6,7,8,9,10)

def test_reverse_linked_list():
    linked.reverse()
    assert linked.show() == [10,9,8,7,6,5,4,3,2,1], "Failed: reverse linked list"

def test_find_middle():
    # Odd length — clear middle
    ll = SinglyLinkedList(1, 2, 3, 4, 5)
    assert ll.middle().data == 3, "Failed: odd length"

    # Even length — second middle
    ll2 = SinglyLinkedList(1, 2, 3, 4)
    assert ll2.middle().data == 3, "Failed: even length"

    # Single node
    ll3 = SinglyLinkedList(1)
    assert ll3.middle().data == 1, "Failed: single node"

    # Two nodes — second middle
    ll4 = SinglyLinkedList(1, 2)
    assert ll4.middle().data == 2, "Failed: two nodes"


def test_has_cycle():
    # No cycle — normal list
    ll = SinglyLinkedList(1, 2, 3, 4, 5)
    assert ll.has_cycle() == False, "Failed: no cycle"

    # Single node, no cycle
    ll2 = SinglyLinkedList(1)
    assert ll2.has_cycle() == False, "Failed: single node no cycle"

    # Empty list
    ll3 = SinglyLinkedList()
    assert ll3.has_cycle() == False, "Failed: empty list"

    # Cycle — tail points back to head
    ll4 = SinglyLinkedList(1, 2, 3, 4, 5)
    ll4.tail.next = ll4.head
    assert ll4.has_cycle() == True, "Failed: cycle to head"

    # Cycle — tail points back to middle
    ll5 = SinglyLinkedList(1, 2, 3, 4, 5)
    ll5.tail.next = ll5.get(2)  # points back to node with value 3
    assert ll5.has_cycle() == True, "Failed: cycle to middle"
