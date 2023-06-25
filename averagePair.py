# Given a sorted array of integers and a target average, determine if there is a pair of values in the array 
# where the average of the pair equals the target average. 
# There may be more than one pair that matches the average target.
# averagePair([1,2,3],2.5) // true
# averagePair([1,3,3,5,6,7,10,12,19],8) // true
# averagePair([-1,0,3,4,5,6], 4.1) // false
# averagePair([],4) // false
# solve using Multiple Pointers
# This is more like divide and conquer
def averagePair(arr, avg):
    if len(arr) <= 1:
        print("Invalid input")
        return False
    left = 0
    right = len(arr)-1
    while (right > 0 and left < len(arr)-1):
        localavg = (arr[left]+arr[right])/2
        if localavg == avg:
            print(arr[left], arr[right])
            left += 1
            right -= 1
        elif localavg < avg:
            left += 1
        elif localavg > avg:
            right -= 1

averagePair([1, 3, 4, 2, 4, 6, 7, 5], 3)
#averagePair([1, 3, 3, 5, 6, 7, 10, 12, 19] ,8)
#averagePair([1,2,3],2.5)
#averagePair([],4)
#averagePair([-1,0,3,4,5,6], 4.1)
