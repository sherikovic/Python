# Find a pair with the given sum in an array
def findPairWithAGivenSum(arr, target):
    # Solution A:
    # for i in range(len(arr)-1):
    #     for j in range(i+1, len(arr)):
    #         if arr[i]+arr[j]==target:
    #             print("Numbers are: ", arr[i], "and ", arr[j])

    # Solution B:
    arr.sort(reverse=True)
    start, end = 0, len(arr) - 1
    while start < end:
        if arr[start] + arr[end] == target:
            print("Numbers are: ", arr[start], "and ", arr[end])
            start = start + 1
            end = end - 1
        elif arr[start] + arr[end] > target:
            start = start + 1
        else:
            end = end - 1


# arr = [8, 7, 2, 5, 3, 1, 10, 0]
# target = 10
# findPairWithAGivenSum(arr, target)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# Print all subarrays with 0 sum, contiguous numbers only
def findSubArrayWithZeroSum(arr):
    for i in range(len(arr)):
        sum = arr[i]
        for j in range(i + 1, len(arr)):
            sum += arr[j]
            if sum == 0:
                print("Array is between ", [k for k in arr[i : j + 1]])


# arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
# findSubArrayWithZeroSum(arr)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# Sort binary array in linear time O(N) and constant space O(1)
def sortBinaryArray(arr):
    zeroCounts = arr.count(0)
    for i in range(zeroCounts):
        arr[i] = 0
    for i in range(zeroCounts, len(arr)):
        arr[i] = 1


# arr = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
# sortBinaryArray(arr)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# Find the duplicate element in a limited range array, space O(1)
def findDuplicateElement(arr):
    # Solution A:
    # Time complexity: O(N^2)
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                print("Number ", arr[i], "at index ", i, " is duplicated at index ", j)


# arr = [1, 3, 2, 3, 4, 2]
# findDuplicateElement(arr)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# Find the largest sub-array formed by consecutive integers
# all elements should be distinct
def findLargestIntSubarray(arr):
    i, j, size = 0, 1, 0
    idx = None
    numsCollected = []
    numsCollected.append(0)
    while i < len(arr) and j < len(arr):
        if arr[j] not in numsCollected:
            numsCollected.append(arr[j])
            j += 1
        else:
            numsCollected.clear()
            numsCollected.append(arr[j])
            if j - i - 1 > size:
                size = j - i
                idx = [i, j - 1]
            i += 1
            j += 1
    if size != 0:
        print(
            "Largest subarray is of size ",
            size,
            "and starts from index ",
            idx[0],
            "till index ",
            idx[1],
        )
    else:
        print("Somehow size turns out to be zero!")


# arr = [2, 0, 2, 1, 4, 3, 1, 0]
# findLargestIntSubarray(arr)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# Find maximum length sub-array having a given sum
def findMaxLenSubarrayWithAGivenSum(arr, target):
    i, j, size, sum, idx = 0, 1, 0, arr[0], None
    while i < len(arr) and j < len(arr):
        sum += arr[j]
        if sum == target:
            if j - i - 1 > size:
                size = j - i
                idx = [i, j]
        elif sum > target:
            i += 1
            j = i + 1
            sum = arr[i]
        else:
            j += 1
    if size != 0:
        print(
            "Target was reached by accumulating numbers between ",
            idx[0],
            "and ",
            idx[1],
        )
    else:
        print("No match found :(")


# arr = [5, 6, -5, 5, 3, 5, 3, -2, 0]
# target = 8
# findMaxLenSubarrayWithAGivenSum(arr, target)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
