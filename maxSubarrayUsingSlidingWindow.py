######### SLIDING WINDOW #########
# Same function as maxSubarraySum but using sliding window approach
# Basically create a window and move it along the array, so instead of looping twice over the array
# this adds the new number and substracts the previous one to increae efficienct
# O(N)
def maxSubarrayUsingSlidingWindow(arr, num):
    if len(arr) < num:
        return "Wrong length"
    max = 0
    sum = 0
    for i in range(0, num):
        sum += arr[i]
    max = sum
    for i in range(num, len(arr)):
        sum = sum + arr[i] - arr[i-num]
        if sum > max:
            max = sum
    return max

print(maxSubarrayUsingSlidingWindow([2, 4, 2, 4, 7, 1, 8, 9], 2))