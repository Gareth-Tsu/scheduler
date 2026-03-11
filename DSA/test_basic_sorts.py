from basic_sorts import *
from SLL import *


def test_buble_sort():
    assert bubbleSort([5,4,3,2,1]) == [1,2,3,4,5]



def test_selection_sort():
    assert selectionSort([5,4,3,2,1]) == [1,2,3,4,5]

def test_insertion_sort():
    assert insertionSort([5,4,3,2,1]) == [1,2,3,4,5]
    assert insertionSort([2,1,3,4,5]) == [1,2,3,4,5]


def test_merge_sort():
    assert mergesort([5,4,3,2,1,6]) == [1,2,3,4,5,6]