# big numbers bubble at the end
# with every comparison, swap to the right so that big numbers end up at the end
# after every iteration the biggest number will appear at the end
# O(N) - O(N^2)
def bubbleSort(arr):
    size = len(arr)
    stillSwapping = True
    # for i in range(len(arr), 0, -1):
    #     for j in range(0, i-1):
    while size > 0 and stillSwapping is True:
        stillSwapping = False
        for i in range(size-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                stillSwapping = True # if no swapping happened, it means the list is already ordered
        size -= 1
    return arr
# print(bubbleSort([5, 3, 2, 1, 6, 7]))
# print(bubbleSort([0, 2, 5, 10, 8, 15])) # you can test the stillSwapping effectiveness with this example

# Looks for the minimum and swaps it with the first number
# worse than bubble sort, may be better than it if you wanna minimize the number of swaps, since you only swap once
# O(N^2)
def selectionSort(arr):
    for j in range(len(arr)):
        minPos = j
        for i in range(j+1, len(arr), 1):
            if arr[i] < arr[minPos]:
                minPos = i
        if j != minPos:
            arr[minPos], arr[j] = arr[j], arr[minPos]
    return arr


# print(selectionSort([-4, 1, 5, 3, 2, 1, 6, -3, 7]))


# start from the beginning and compare elements to whatever is behind it as you swap it
# 12, 11, 13, 5, 6
# 11, 12, 13, 5, 6
# 11, 12, 13, 5, 6
# 11, 12, 5, 13, 6
# 11, 5, 12, 13, 6
# 5, 11, 12, 13, 6
# O(N) - O(N^2)
def insertionSort(arr):
    for i in range(1, len(arr), 1):
        currentPos = i
        for j in range(i-1, -1, -1):
            if arr[currentPos] < arr[j]:
                arr[currentPos], arr[j] = arr[j], arr[currentPos]
                currentPos -= 1
            else:
                break
    return arr


# print(insertionSort([-4, -7, 5, 3, 2, 1, 6, -3, 7]))


# break down your array to single item arrays, merge them back into two item arrays
# sort them and then merge them back and so on
# O(nlogn)
# O(n)
def mergeSort(arr):
    def mergeTwoSortedArrays(arr1, arr2):
        totalArr = []
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                totalArr.append(arr1[i])
                i += 1
            else:
                totalArr.append(arr2[j])
                j += 1
        if i is len(arr1) and j is not len(arr2):
            totalArr += arr2[j:]
        elif i is not len(arr1) and j is len(arr2):
            totalArr += arr1[i:]
        return totalArr

    from math import floor
    if len(arr) <= 1:
        return arr
    half = floor(len(arr)/2)
    left = mergeSort(arr[0:half])
    right = mergeSort(arr[half:])
    return mergeTwoSortedArrays(left, right)
# print(mergeSort([2, 3, 4, 5, 1, 11, 32, 29, 7, 3]))


# This algorithm chooses a pivot and moves all the numbers less than it to the left of it
# and all the numbers greater than it to the right of it
# then swaps that element to the correct spot
# Repeats the same to all the array members
# swap the element less than your pivot with the one following your pivot
# for exmaple: 11 23 54 66 34 9 14 1
# 11 is the pivot
# swap 9 with 23
# 11 9 54 66 34 23 14 1
# swap 1 with 54
# 11 9 1 66 34 23 14 54
# now swap 11 with 1, which is the last element that is less than the pivot
# 1 9 11 66 34 23 14 54
# O(NlogN) - O(N^2)
# O(N)
# this is based on choosing the first element as the pivot
def quickSort(arr, left, right):
    def sortPivot(arr, start, end):
        pivot = arr[start]
        swapIdx = start  # because this is where your pivot is, so you wanna swap this with the correct position
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
# n = len(arr)
# print(quickSort(arr, 0, n))


# THIS IS NOT THE OPTIMAL ALGO SOLUTION
# def quickSort(arr):
#     def findPivot(pvtidx):
#         pivotNum = arr[pvtidx]
#         pivotIdx = pvtidx
#         stillSwapping = False
#         for i in range(pvtidx+1, len(arr)):
#             if arr[i] < pivotNum:
#                 stillSwapping = True
#                 pivotIdx += 1
#                 arr[i], arr[pivotIdx] = arr[pivotIdx], arr[i]
#         arr[pvtidx], arr[pivotIdx] = arr[pivotIdx], arr[pvtidx]
#         if stillSwapping:
#             findPivot(arr, pvtidx)

#     pivotIdx = 0
#     while pivotIdx < len(arr)-1:
#         findPivot(pivotIdx)
#         pivotIdx += 1

#     return arr


# quickSort([5, 2, 1, 6, 7, 8, 3, 4])
# quickSort([32, 20, 14, 68, 44, -82, 24, 45])


# this depends on calssifying each digit into the correct bucket
def getDigit(num, i):
    from math import floor, pow
    return floor(abs(num) / pow(10, i)) % 10

# getDigit(3261, 2)


def digitCount(num):
    if num == 0:
        return 1
    from math import floor, log10
    return floor(log10(abs(num)))+1

# digitCount(1)


def maxDigits(nums):
    maxNum = 0
    for num in nums:
        maxNum = max(maxNum, digitCount(num))
    return maxNum

# O(nk) - n: length of array, k: number of digits
# O(n+k)


def radixSort(arr):
    maxDigitCount = maxDigits(arr)
    for k in range(maxDigitCount):
        digitBuckets = {}
        for i in range(len(arr)):
            digit = getDigit(arr[i], k)
            if digit not in digitBuckets.keys():
                digitBuckets[digit] = list()
            digitBuckets[digit].append(arr[i])
        arr = list()
        for j in range(10):
            if j in digitBuckets.keys():
                arr += digitBuckets[j]
    return arr

# print(radixSort([23, 9, 124, 7457, 111, 1317, 141, 5262]))
