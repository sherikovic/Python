# This function will return the max sum found of the number of integers in arr given with num
# O(N^2)
def maxSubarraySum(arr, num):
    max = 0
    for i in range(len(arr)-num+1):
        sum = 0
        for j in range(i, i+num):
            sum += arr[j]
            if sum > max:
                max = sum
    return max

print(maxSubarraySum([1, 2, 4, 9, 5, 2, 3], 2))
