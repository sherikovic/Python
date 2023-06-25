# Accepts two parameters - an array of positive integers and a positive integer
# Return the minimal length of a contiguous subarray of which the sum is greater than or equal to the 
# integer passed to the function. If there isn't one, return 0 instead.
# minSubArrayLen([2,3,1,2,4,3], 7) // 2 -> because [4,3] is the smallest subarray
# minSubArrayLen([2,1,6,5,4], 9) // 2 -> because [5,4] is the smallest subarray
# minSubArrayLen([3,1,7,11,2,9,8,21,62,33,19], 52) // 1 -> because [62] is greater than 52
# minSubArrayLen([1,4,16,22,5,7,8,9,10], 55) // 5
# minSubArrayLen([4, 3, 3, 8, 1, 2, 3], 11) // 2
# Sliding window - O(N)
def minSubArrayLen(arr, num):
    i = 0
    j = 0
    sum = 0
    leastnum = 0
    leastList = []
    flag = False
    while i < len(arr)-1:
        if arr[j] >= num:
                leastnum = 1
                leastList = [arr[j]]
                break
        elif sum < num and j <= len(arr)-1 and flag is False:
            sum += arr[j]
            if j is not len(arr)-1:
                j += 1
            else:
                flag = True
        elif sum >= num:
            if leastnum == 0 or leastnum > j-i+1:
                   leastnum = j-i+1
                   leastList = [arr[i], arr[j]]
            sum -= arr[i]
            if i is not len(arr)-1:
                i += 1
        else:
             break
    print(leastList)
    print(leastnum)
    return leastnum

minSubArrayLen([2,3,1,2,4,3], 7)
minSubArrayLen([2,1,6,5,4], 9)
minSubArrayLen([3,1,7,11,2,9,8,21,62,33,19], 52)
minSubArrayLen([1,4,16,22,5,7,8,9,10], 55)
minSubArrayLen([4, 3, 3, 8, 1, 2, 3], 11)
