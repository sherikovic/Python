# Merge two sorted linked lists from their end
# Write a function that takes two lists, each of which is sorted in increasing order,
# and merges the two into one list, which is in decreasing order, and returns it.
# In other words, merge two sorted linked lists from their end.
# a = {1, 3, 5} and b = {2, 6, 7, 10} => {10, 7, 6, 5, 3, 2, 1}
class Node:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next


class singlyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def moveNode(self, insertedNode, afterNode, beforeNode):
        if beforeNode == None:  # means it is a head
            insertedNode.next = afterNode  # or self.head
            self.head = insertedNode
        else:
            insertedNode.next = afterNode
            beforeNode.next = insertedNode

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        count = 0
        prev = None
        while count < self.length:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
            count += 1


def mergeTwoSinglyLinkedLists(sllA, sllB):
    currentA = sllA.head
    currentB = sllB.head
    sllAB = singlyLinkedList()
    while currentA and currentB:
        if currentA.val > currentB.val:  # < with reverse
            sllAB.push(currentA.val)
            currentA = currentA.next
        elif currentA.val < currentB.val:  # > with reverse
            sllAB.push(currentB.val)
            currentB = currentB.next
        else:
            sllAB.push(currentA.val)
            sllAB.push(currentB.val)
            currentA = currentA.next
            currentB = currentB.next

    while currentA:
        sllAB.push(currentA.val)
        currentA = currentA.next
    while currentB:
        sllAB.push(currentB.val)
        currentB = currentB.next

    # sllAB.reverse()
    return sllAB

# arrA = [1, 3, 5]
# arrB = [2, 6, 7, 10]
# sllA = singlyLinkedList()
# sllB = singlyLinkedList()
# [sllA.push(a) for a in reversed(arrA)]
# [sllB.push(b) for b in reversed(arrB)]
# mergeTwoSinglyLinkedLists(sllA, sllB)


# Given a collection of n items, each of which has a non-negative integer key
# whose maximum value is at most k, effectively sort it using the counting sort algorithm.
# USING Counting Sort
# arr: [4, 2, 10, 10, 1, 4, 2, 1, 10]
# freq: [0 2 2 0 2 0 0 0 0 0 3]
def countSort(arr, k):
    output = [0] * len(arr)
    freq = [0] * (k+1)
    # count the occurances of each number in arr
    for i in arr:
        freq[i] += 1
    # calculate the starting index of each number
    total = 0
    for i in range(k+1):
        oldCount = freq[i]
        freq[i] = total
        total += oldCount
    # sort them, use the numbers in arr as an index to freq
    for i in arr:
        output[freq[i]] = i
        freq[i] += 1

    arr = output

    return arr


# print(countSort([4, 2, 10, 10, 1, 4, 2, 1, 10], 10))

#           j  cp
# 0: 5, 3, 44, 2, 23, 11, 6
# 1: 3, 5, 44, 2, 23, 11, 6
# 2: 3, 5, 44, 2, 23, 11, 6
# 3: 3, 5, 2, 44, 23, 11, 6
# 4:
def insertionSort(arr):
    for i in range(1, len(arr), 1):
        currentVal = arr[i]
        currentPos = i
        for j in range(i-1, -1, -1):
            if arr[j] > currentVal:
                arr[j], arr[currentPos] = arr[currentPos], arr[j]
                currentPos -= 1
            else:
                break
    return arr


# print(insertionSort([3, 5, 33, 12, -20, 2, 6]))


# 0: 5, 3, 44, 2, 23, 11, 6
# 1: 5, 3, 2, 23, 11, 6, 44
# 2: 5, 3, 2, 11, 6, 23, 44
# 3: 5, 3, 2, 6, 11, 23, 44
# 4: 3, 2, 5, 6, 11, 23, 44
# 5: 2, 3, 5, 6, 11, 23, 44
def bubbleSort(arr):
    size = len(arr)
    stillSwapping = True
    while size > 0 and stillSwapping is True:
        stillSwapping = False
        for i in range(1, size, 1):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                stillSwapping = True
        size -= 1
    return arr


# print(bubbleSort([32, 0, 1, 2, 44, 20, 14, 68, -82, 24, 45]))
# print(bubbleSort([32, -82, 0, 1, 2, 20, 24, 44, 45, 68]))


def selectionSort(arr):
    stillSwapping = True
    if stillSwapping is True:
        for i in range(len(arr)):
            minPos = i
            stillSwapping = False
            for j in range(i+1, len(arr), 1):
                if arr[minPos] > arr[j]:
                    minPos = j
                    stillSwapping = True
            if minPos is not i:
                arr[minPos], arr[i] = arr[i], arr[minPos]
    return arr


# print(selectionSort([32, 0, 1, 2, 44, 20, 14, 68, -82, 24, 45]))
# print(selectionSort([32, -82, 0, 1, 2, 20, 24, 44, 45, 68]))


# 5, 3, 6, 44, 2, 2, 2, 23, 11, 6
def quickSort(arr, left, right):
    def sortPivot(arr, start, end):
        pivot = arr[start]
        swapIdx = start
        for i in range(start+1, end):
            if pivot >= arr[i]:
                swapIdx += 1
                arr[swapIdx], arr[i] = arr[i], arr[swapIdx]
        arr[start], arr[swapIdx] = arr[swapIdx], arr[start]
        return swapIdx

    if left < right:
        pvtIdx = sortPivot(arr, left, right)
        leftSide = quickSort(arr, left, pvtIdx)
        rightSide = quickSort(arr, pvtIdx+1, right)

    return arr


# arr = [5, 3, 6, 44, 2, 2, 2, 23, 11, 101, 6, -62]
# print(quickSort(arr, 0, len(arr)))


def mergeSort(arr):
    def mergeTwoArrays(arr1, arr2):
        mergedArray = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                mergedArray.append(arr1[i])
                i += 1
            else:
                mergedArray.append(arr2[j])
                j += 1
        if i < len(arr1) and j is len(arr2):
            mergedArray += arr1[i:]
        elif i is len(arr1) and j < len(arr2):
            mergedArray += arr2[j:]
        return mergedArray

    if len(arr) <= 1:
        return arr

    from math import floor
    leftArray = mergeSort(arr[0:floor(len(arr)/2)])
    rightArray = mergeSort(arr[floor(len(arr)/2):len(arr)])
    return mergeTwoArrays(leftArray, rightArray)


# print(mergeSort([5, 3, 6, 44, 2, 2, 2, 23, 11, 101, 6, -62]))
