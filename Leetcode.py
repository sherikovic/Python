#-------------------------------------------------------#
#--------------- Find the Pivot Interger ---------------#
#-------------------------------------------------------#
def pivotInteger(n):
    # if n == 1: return 1
    # pivot = 2
    # while pivot <= n:
    #     leftsum = 0
    #     rightsum = 0
    #     for l in range(1, pivot+1):
    #         leftsum += l
    #     for r in range(pivot, n+1):
    #         rightsum += r
    #         if rightsum > leftsum: break
    #     if leftsum == rightsum:
    #         return pivot
    #     pivot += 1
    # return -1

    # l = 1
    # r = n
    # sum = n * (n + 1) / 2
    # while l < r:
    #     m = (l + r) / 2
    #     if m * m - sum < 0:
    #         l = m + 1
    #     else:
    #         r = m
    # if l * l - sum == 0: return l
    # else: return -1

    for i in range(1, n+1):
        leftsum = i * (i + 1)
        rightsum = n * (n + 1) - i * (i - 1)
        if leftsum == rightsum:
            return i
    return -1

# nums = [1, 4, 8]
# for num in nums:
#     print(pivotInteger(num))


#-------------------------------------------------------#
#----------------------- Two Sum -----------------------#
#-------------------------------------------------------#
def twoSum(nums, target):
    # O(n2)
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if (nums[i] + nums[j]) == target:
    #             return(i, j)

    # O(nlogn)
    # nums.sort()
    # l = 0
    # r = len(nums) - 1
    # while l < r:
    #     if nums[l] + nums[r] > target: r -= 1
    #     elif nums[l] + nums[r] < target: l += 1
    #     else: return nums[l], nums[r]

    # O(n)
    hashtable = {}
    for i in range(len(nums)):
        hashtable[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashtable and complement is not nums[i]:
            return i, hashtable[complement]

    # O(n)
    # hashtable = {}
    # for i in range(len(nums)):
    #     complement = target - nums[i]
    #     if complement in hashtable:
    #         return i, hashtable[complement]
    #     hashtable[nums[i]] = i

# print(twoSum([12, 2, 7, -3, 15], 9))
# print(twoSum([3, 2, 4], 6))



#-------------------------------------------------------#
#------------------- Add Two Numbers -------------------#
#-------------------------------------------------------#
class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None

class singlyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self
    def pop(self):
        if not self.head: return None
        previous = None
        current = self.head
        while current.next:
            previous = current
            current = current.next
        self.tail = previous
        if self.tail: self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current.val
    def printList(self):
        ptr = self.head
        while ptr:
            if ptr.next:
                print(ptr.val, end=" -> ")
            else:
                print(ptr.val)
            ptr = ptr.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createList(nums):
    # ll = singlyLinkedList()
    # for num in nums:
    #     ll.push(num)
    # return ll

    node0 = ListNode()
    res = node0
    for num in nums:
        newNode = ListNode(num)
        node0.next = newNode
        node0 = newNode
    return res.next

# add the heads of both lists
# move forward towards the tails
def addTwoNumbers(l1, l2):
    # This is using a traditional singly list
    # numbers are reversed ie start from the tail
    # 2 -> 4 -> 3 == 342

    # num1, num2 = "", ""
    # for i in range(l1.length): num1 = num1 + str(l1.pop())
    # for i in range(l2.length): num2 = num2 + str(l2.pop())
    # sum = int(num1) + int(num2)
    # lsum = reversed(list(map(int, str(sum))))
    # lsum = createList(lsum)
    # lsum.printList()

    # This is using the singly list given by leetcode
    # It doesn't have head, tail or a separate list class, just nodes
    # This is is why it is essential to create a dummy node in the beginning to start with
    node0 = ListNode()
    res = node0
    total = carry = 0
    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next

        num = total % 10
        carry = total // 10

        node0.next = ListNode(num)
        node0 = node0.next

    return res.next

# l1 = createList([2, 4, 3])
# l2 = createList([7, 6, 4])
# addTwoNumbers(l1, l2)

#--------------------------------------------------------#
#---- Longest Substring Without Repeating Characters ----#
#--------------------------------------------------------#
def lengthOfLongestSubstring(s: str) -> int:
    i = 0
    j = 0
    maxLen = 0
    shash = {}
    if len(s) == 0: return 0
    if len(s) == 1: return 1
    if s == " ": return 1
    while j < len(s):
        if i < len(s) and s[i] not in shash:
            shash[s[i]] = 1
            if i is not len(s): i += 1
        else:
            maxLen = max(maxLen, abs(j - i))
            shash = {}
            j += 1
            i = j
    print(maxLen)

lengthOfLongestSubstring("abcabcbb")
lengthOfLongestSubstring("abcvdbuewihrna")
lengthOfLongestSubstring("dfdv")

