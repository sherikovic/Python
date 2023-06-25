# Taken out from https://www.geeksforgeeks.org/searching-algorithms

# find two elements whose sum is closest to zero
#   i
# 5 3 1 7 9 1 2 8 6 1 0
#         j
def SumClosestToZero(arr):
    firstidx, secondidx, k = 0, 1, 2
    sum = arr[firstidx] + arr[secondidx]
    while k < len(arr):
        if arr[k] < arr[firstidx] or arr[k] < arr[secondidx]:
            firstidx = arr.index(min(arr[firstidx], arr[secondidx]))
            secondidx = k
            sum = arr[firstidx] + arr[secondidx]
        k += 1
    return sum

# print(SumClosestToZero([5, 3, 3, 7, 9, 1, 0, 2, 8, 6, 5]))


#     i
# 5 3 8 7 9 1 2 8 6 1 0
#       j
def pairWithAGivenDiff(arr, num):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i]-arr[j]) == num:
                result.append([arr[i], arr[j]])
                print("Found one pair [%s, %s] at [%s, %s]" %
                      (arr[i], arr[j], i, j))
    return result

# print(pairWithAGivenDiff([5, 3, 8, 7, 9, 1, 2, 8, 6, 1, 0], 6))

# i
# 2 4 15 27 48 99
#   j


def pairWithAGivenDiffSorted(arr, num):
    i, j = 0, 1
    while i < len(arr) and j < len(arr):
        diff = arr[j] - arr[i]
        if num == diff:
            return True
        elif num > diff:
            j += 1
        else:
            i += 1
    return False

# print(pairWithAGivenDiffSorted([2, 4, 15, 27, 48, 99], 21))

# find common elements in three sorted arrays
#     i
# 2 4 5 7 8 9
#         j
# 1 2 3 4 7 9
#       k
# 0 3 4 5 8 9


def findCommonElements(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    matches = []
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            matches.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    return matches
    # match = False
    # for i in range(len(arr1)):
    #     for j in range(i,len(arr2)):
    #         if arr1[i] == arr2[j]:
    #             match = True
    #     for k in range(i,len(arr3)):
    #         if arr1[i] == arr3[k] and match is True:
    #             matches.append(arr1[i])


# arr1 = [0, 1, 4, 5, 7, 8, 9]
# arr2 = [0, 2, 3, 4, 5, 9]
# arr3 = [1, 4, 5, 6]
# print(findCommonElements(arr1, arr2, arr3))

# i
# 4 3 66 12 54 66 90 98 2 2 87
#   j
def firstRepeatingNumber(arr):
    elements = {}
    for i in range(len(arr)):
        if arr[i] not in elements.keys():
            elements[arr[i]] = 1
        else:
            print("This number %s already exists." % (arr[i]))

# firstRepeatingNumber([4, 3, 66, 12, 54, 66, 90, 98, 2, 2, 87])

#     i
# 4 3 12 54 66 90 98 2 87
#        j
#          k


def largestPairSum(arr):
    i, j, k = 0, 1, 2
    sum = arr[i] + arr[j]
    for k in range(len(arr)):
        if arr[i] > arr[j]:
            idxOfBiggestNumberOfCurrentSum = i
        elif arr[j] > arr[i]:
            idxOfBiggestNumberOfCurrentSum = j

        if arr[idxOfBiggestNumberOfCurrentSum] + arr[k] > sum:
            i = idxOfBiggestNumberOfCurrentSum
            j = k
            sum = arr[i] + arr[j]
    return sum

# print(largestPairSum([4, 3, 66, 12, 54, 66, 90, 87, 2, 2, 98]))

# i
# 0 -1 2 -3 1
#    j
#      k


def findTripletsWithZeroSum(arr):
    # for i in range(len(arr)-2):
    #     for j in range(i+1, len(arr)-1):
    #         for k in range(j+1, len(arr)):
    #             if arr[i] + arr[j] + arr[k] == 0:
    #                 print(arr[i], arr[j], arr[k])

    arr.sort()
    for i in range(len(arr)-2):
        l = i+1
        r = len(arr)-1
        while l < r:
            if arr[i] + arr[l] + arr[r] == 0:
                print(arr[i], arr[l], arr[r])
                l += 1
                r -= 1
            elif arr[i] + arr[l] + arr[r] > 0:
                r -= 1
            else:
                l += 1

# findTripletsWithZeroSum([0, -1, 2, -3, 1, 6, -6, 0])


# Given an array, find an element before which all elements are smaller than it,
# and after which all are greater than it.
#         i
# 5 1 4 3 6 8 10 7 9
#       l   r
def findPivot(arr):
    # l, r = -1, -1
    # for i in range(len(arr)):
    #     if i != 0:
    #         l = i-1
    #     if i != len(arr)-1:
    #         r = i+1
    #     while l > 0 or r < len(arr)-1:
    #         if arr[l] < arr[i] and l != 0:
    #             l -= 1
    #         if arr[r] > arr[i] and r != len(arr)-1:
    #             r += 1
    #         if arr[l] > arr[i] or arr[r] < arr[i]:
    #             break
    #         if l == 0 and r == len(arr)-1:
    #             print(arr[i])
    # return -1

    leftMax = [None] * len(arr)
    leftMax[0] = arr[0]
    for i in range(1, len(arr)):
        leftMax[i] = max(leftMax[i-1], arr[i-1])

    rightMin = [None] * len(arr)
    rightMin[len(arr)-1] = arr[len(arr)-1]
    for i in range(len(arr)-2, -1, -1):
        rightMin[i] = min(rightMin[i+1], arr[i])

    for i in range(1, len(arr)-1):
        if leftMax[i-1] <= arr[i] and arr[i] <= rightMin[i+1]:
            return i

    return -1


findPivot([5, 1, 4, 3, 8, 6, 10, 7, 9])


def binarySearch(arr, num):
    from math import floor
    start = 0
    end = len(arr) - 1
    middle = floor((start + end)/2)
    while arr[middle] != num and start <= end:
        if arr[middle] > num:
            end = middle - 1
        else:
            start = middle + 1
        middle = floor((start + end)/2)
    if arr[middle] == num:
        return middle
    return -1

# print(binarySearch([0, 1, 4, 5, 7, 8, 9], 7))


# Given an array with all distinct elements, find the largest three elements.
# i
# 10 4 3 50 23 90
#    j
def findThreeLargestNumbers(arr):
    max1, max2, max3 = 0, 0, 0
    for i in range(0, len(arr)):
        if arr[i] > max1:
            max3 = max2
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max3 = max2
            max2 = arr[i]
        elif arr[i] > max3:
            max3 = arr[i]
    print(max1, max2, max3)

# findThreeLargestNumbers([10, 4, 3, 50, 23, 90])


# Given an unsorted array of size n. Array elements are in the range of 1 to n.
# One number from set {1, 2, …n} is missing and one number occurs twice in the array.
def findMissingAndRepeatingNum(arr, n):
    elems = {}
    for i in range(len(arr)):
        if arr[i] not in elems.keys():
            elems[arr[i]] = 1
        else:
            elems[arr[i]] += 1
    print("Repeating item is: %s" %
          [k for k in elems.items() if k[1] > 1][0][0])
    orgSum = n*(n+1)/2
    sum = 0
    for item in elems.items():
        sum += item[0]
    print("Missing number is: %d" % (orgSum-sum))

# findMissingAndRepeatingNum([7, 3, 4, 5, 5, 6, 2], 7)


# Given a binary array arr[] of size N, which is sorted in
# non-increasing order, count the number of 1’s in it.
def countOnes(arr):
    from math import floor
    start = 0
    end = len(arr)-1
    if arr[0] == 0:
        return -1
    while start <= end:
        mid = floor((start+end)/2)
        if arr[mid] == 1 and arr[mid+1] == 0:
            return mid+1
        elif arr[mid+1] == 1:
            start = mid + 1
        else:
            end = mid - 1

# print(countOnes([1, 1, 0, 0, 0, 0, 0]))


# Write an efficient program for printing K largest elements in an array.
# Elements in an array can be in any order
# Input:  [1, 23, 12, 9, 30, 2, 50], K = 3
# Output: 50, 30, 23
# Input:  [11, 5, 12, 9, 44, 17, 2], K = 2
# Output: 44, 17
def findKLargestElements(arr, k):
    temp = [arr[0], arr[1], arr[2]]
    minTemp = min(temp)
    for i in range(3, len(arr)-1):
        if arr[i] > minTemp:
            temp[temp.index(minTemp)] = arr[i]
            minTemp = min(temp)
    return temp

# print(findKLargestElements([11, 5, 12, 9, 44, 17, 2], 3))


# Given an n x n matrix, where every row and column is sorted in non-decreasing order.
# Find the kth smallest element in the given 2D array.
# Input:k = 3 and array =
#         10, 20, 29, 40
#         15, 25, 35, 45
#         24, 32, 37, 48
#         30, 33, 39, 50
# Output: 20
# Explanation: The 3rd smallest element is 20
# ROW:COl
#   1:1
#   2:1
#   1:2
#   3:1
#   2:2
#   1:3
#   4:1
#   3:2
#   2:3
#   1:4
#   4:2
#   3:3
#   2:4
#   4:3
#   3:4
#   4:4
def kthSmallestinMatrix(arr, n, k):
    entries = 0
    found = False
    rn, r, cn, c = 1, 1, 1, 1
    pastItems = []
    while ~found:
        while r >= rn and c <= cn:
            entries += 1
            if entries < k:
                pastItems.append(arr[r-1][c-1])
            else:
                found = True
                return arr[r-1][c-1]
            r -= 1
            c += 1
        if (r == 0 and (c >= 2 or c <= n+1)) and ~found:
            rn = 1
            cn += 1
            r = cn
            c = 1

# arr = [[10, 20, 29, 40],
#        [15, 25, 35, 45],
#        [24, 32, 37, 48],
#        [30, 33, 39, 50]]
# print(kthSmallestinMatrix([ [10, 20, 29, 40],
#                             [15, 25, 35, 45],
#                             [24, 32, 37, 48],
#                             [30, 33, 39, 50]], 4, 9))


def kthNumber(mat, k):
    import heapq
    heap = [[mat[i][0], i, 0] for i in range(len(mat))]
    [heapq.heapify(heap) for i in range(len(mat))]
    for i in range(k-1):
        val, row, col = heapq.heappop(heap)
        heapq.heappush(heap, [mat[row][col+1], row, col+1])
    return heapq.heappop(heap[0])

# print(kthNumber([
#                 [10, 20, 30, 40],
#                 [15, 25, 35, 45],
#                 [25, 29, 37, 48],
#                 [32, 33, 39, 50]], 7))


# Given an array of integers which is initially increasing and then decreasing,
# find the maximum value in the array.
def findMaximum(arr):
    start = 0
    end = len(arr)-1
    from math import floor
    while start <= end:
        mid = floor((start + end)/2)
        # 87 100 50
        if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
            return arr[mid]
        # 123 100 50
        elif arr[mid] > arr[mid+1] and arr[mid] < arr[mid-1]:
            end = mid - 1
        # 50 100 123
        elif arr[mid] < arr[mid+1] and arr[mid] > arr[mid-1]:
            start = mid + 1
    return -1

# print(findMaximum([2, 4, 6, 8, 10, 3, 1]))


# Given an array and a number K where K is smaller than the size of the array.
# Find the K’th smallest element in the given array.
# Given that all array elements are distinct.
def kthSmallest(arr, k):
    import heapq
    if k > len(arr):
        return -1
    heap = []
    for i in range(k):
        heapq.heappush(heap, arr[i])
        heapq._heapify_max(heap)
    for i in range(k, len(arr)):
        if arr[i] < heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, arr[i])
            heapq._heapify_max(heap)
    return heap[0]

# print(kthSmallest([10, 5, 4, 3, 48, 6, 2, 33, 53, 10], 9))


# Given a sorted and rotated array arr[] of size N and a key,
# the task is to find the key in the array.
# 5, 6, 7, 8, 9, 10, 1, 2, 3
def findNumInSortedAndRotatedArray(arr, num):
    start = 0
    end = len(arr)
    from math import floor
    pivot = None
    while start < end:
        mid = floor((start+end)/2)
        if arr[mid] < arr[mid-1]:
            pivot = mid - 1
            break
        elif arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
            pivot = mid
            break
        elif arr[start] >= arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if num >= arr[0] and num < arr[pivot]:
        start = 0
        end = pivot
    else:
        start = pivot + 1
        end = len(arr)-1
    while start <= end:
        mid = floor((start+end)/2)
        if arr[mid] < num:
            start = mid + 1
        elif arr[mid] > num:
            end = mid - 1
        else:
            return mid


# print(findNumInSortedAndRotatedArray([5, 6, 7, 8, 9, 10, 11, 1, 2, 3], 10))


# i
# 5, 3, 6, 44, 2, 2, 2, 23, 11, 101, 6, -62
# 1, 2, 3, 4, 5, 6, 7
#       j
def findThePeakElement(arr):
    mightBeDecreasing, mightBeIncreasing = 0, 0
    i, j = 0, 2
    peakElements = []
    while j < len(arr):
        if arr[i+1] > arr[i] and arr[i+1] > arr[j]:
            peakElements.append(arr[i+1])
        elif arr[i] > arr[i+1] and arr[i+1] > arr[j]:
            mightBeDecreasing += 1
        elif arr[i] < arr[i+1] and arr[i+1] < arr[j]:
            mightBeIncreasing += 1
        i += 1
        j += 1

    if mightBeDecreasing == i:
        return arr[0]
    elif mightBeIncreasing == i:
        return arr[len(arr)-1]

    return peakElements


# print(findThePeakElement([5, 13, 6, 44, 55, 2, 2, 23, 11, 101, 6, -62]))
# print(findThePeakElement([1, 2, 3, 4, 5, 6, 7, 8]))
# print(findThePeakElement([34, 10, 9, 7, 6, 5, 4, 3, 2, 1]))


# the idea is to divide the array to three elements each, two on the left hand side and one on the right
def getMinMax(low, high, arr):
    arr_max = arr[low]
    arr_min = arr[low]

    # If there is only one element
    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return (arr_max, arr_min)

    # If there is only two element
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return (arr_max, arr_min)
    else:
        # If there are more than 2 elements
        mid = int((low + high) / 2)
        arr_max1, arr_min1 = getMinMax(low, mid, arr)
        arr_max2, arr_min2 = getMinMax(mid + 1, high, arr)

    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))


# Driver code
arr = [205, 13, 6, 44, 55, 2, 2, 23, 11, 101, 6, -62]
high = len(arr) - 1
low = 0
arr_max, arr_min = getMinMax(low, high, arr)
print('Minimum element is ', arr_min)
print('nMaximum element is ', arr_max)
