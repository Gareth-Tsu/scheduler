# Learning Basic sorting algorithms
from SLL import SinglyLinkedList

def bubbleSort(arr):
    for i in range(len(arr) - 1, 0 , -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selectionSort(arr):
    for i in range(len(arr)-1):
        min_in = i #minimun index
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_in]:
                min_in = j
        if min_in != i:
            arr[i], arr[min_in] = arr[min_in], arr[i]
    return arr

def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            arr[j] = temp
            j -= 1
    return arr
def bubble_sort(llist):    #practicing sorting linked lists

    if llist.count <= 1:
        return llist
    for i in range(llist.count - 1, -1, -1):
        for j in range(i):
            if llist.get(j).data < llist.get(j + 1).data:
                llist.set(j, llist.get(j+1).data)
                llist.set(j + 1, llist.get(j).data)
    return llist

def __merge(left, right):
    combined = []
    j = 0
    i = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            combined.append(left[i])
            i += 1
        else:
            combined.append(right[j])
            j += 1

    while i < len(left):
        combined.append(left[i])
        i += 1

    while j < len(right):
         combined.append(right[j])
         j += 1
    return combined

def mergesort(lst):
    if len(lst) <= 1:
        return lst
    mid = int(len(lst) / 2)
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    return __merge(left, right)

def quick_sort(lst, left, right):
    def __pivot(sub, pivot, swap):
        if len(sub) <= 1:
            return sub
        pivot = swap
        for i in range((pivot + 1), len(sub)):
            if pivot < sub[i]:
                swap += 1
                sub[i], sub[swap] = sub[swap], sub[i]
        sub[pivot], sub[swap] = sub[swap], sub[pivot]
        return swap
    if len(lst) <= 1:
        return lst
    pivot_index = __pivot(lst, )





linked = SinglyLinkedList(4,2,6,5,1,3)

