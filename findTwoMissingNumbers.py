def findTwoMissingNumbers(arr, n):
    from math import floor
    arrSum = 0
    orgSum = n*(n+1)/2
    for num in arr:
        arrSum += num
    avg = floor((orgSum - arrSum)/2)
    sumSmallerHalf = 0
    sumGreaterHalf = 0
    for i in range(0, n-2):
        if arr[i] <= avg:
            sumSmallerHalf += arr[i]
        else:
            sumGreaterHalf += arr[i]
    OrgSmallerHalf = avg*(avg+1)/2
    OrgGreaterHalf = orgSum - OrgSmallerHalf
    FirstMissingNumber = OrgSmallerHalf - sumSmallerHalf
    SecondMissingNumber = OrgGreaterHalf - sumGreaterHalf
    return FirstMissingNumber, SecondMissingNumber

print(findTwoMissingNumbers([1, 2, 3, 4, 5, 6, 7], 9))
