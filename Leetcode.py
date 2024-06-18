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


# https://leetcode.com/problems/add-two-numbers/
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


# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(s: str) -> int:
    i, j, maxLen = 0, 0, 0
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

    return maxLen

# lengthOfLongestSubstring("abcabcbb")
# lengthOfLongestSubstring("abcvdbuewihrna")
# lengthOfLongestSubstring("dfdv")


# https://leetcode.com/problems/median-of-two-sorted-arrays/
# The overall run time complexity should be O(log (m+n))
# this constraint forces you to use merge sort
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    def mergeTwoSortedArrays(arr1: list[int], arr2: list[int]) -> list:
        outArr = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                outArr.append(arr1[i])
                i += 1
            else:
                outArr.append(arr2[j])
                j += 1
        if i < len(arr1) and j is len(arr2):
            outArr += arr1[i:]
        if j < len(arr2) and i is len(arr1):
            outArr += arr2[j:]
        return outArr

    finalArray = mergeTwoSortedArrays(nums1, nums2)
    if len(finalArray) == 1:
        return finalArray.pop()
    if (len(finalArray) % 2 == 0):
        mid = int(len(finalArray) / 2)
        return float((finalArray[mid-1] + finalArray[mid]) / 2)
    else:
        from math import ceil
        mid = ceil(len(finalArray)/2)
        return finalArray[mid-1]

# median = findMedianSortedArrays([1, 4], [2, 3, 5])
# median = findMedianSortedArrays([2], [])
# median = findMedianSortedArrays([3], [-2, -1])


def fizzBuzz(n: int):
    def checkMultiples(i, m):
        from math import floor
        div = floor(i/m)
        if div * m == i:
            return True
        else:
            return False

    for i in range(1,n+1):
        if checkMultiples(i, 3) and checkMultiples(i, 5):
            print("FizzBuzz")
        else:
            if checkMultiples(i, 3):
                print("Fizz")
            else:
                if checkMultiples(i, 5):
                    print("Buzz")
                else:
                    print(i)

# fizzBuzz(15)

def findRelatives(related: list[str]):
    mat = []
    for i in range(len(related)):
        row = []
        row.append(i)
        for j in range(len(related[i])):
            if i != j and related[i][j] == "1":
                row.append(j)
        mat.append(row)

    groups = [mat[0]]
    iknow = [None, False]
    for i in range(1, len(mat)):
        for k in range(len(groups)):
            for j in range(len(mat[i])):
                if mat[i][j] in groups[k]:
                    iknow = [k, True]
            if iknow[1]:
                groups[iknow[0]] += mat[i]
                iknow = [None, False]
            else:
                groups.append(mat[i])
    groups_set = []
    for group in groups:
        groups_set.append(set(group))
    return groups_set

# print(findRelatives(['1100', '0100', '0010', '0001']))

# 1 1 1 0
# 1 1 0 0
# 0 1 1 0
# 0 0 0 1

# 1 group: [0 1 2]

# iter1:
# [1 0] if either one is in the 1 group, then add them all to it, we will set them later
# if it was [3 4] for example, it is not in 1 group, then they will form 2 group
# then we will end up with 
# 1 group [0 1 2 1 0]
# 2 group [3 4]

# iter2:
# [2 1 3] 2 is in 1 group then add the whole list to it so it becomes [ 0 1 2 1 0 2 1 3]


# https://leetcode.com/problems/longest-palindromic-substring/
def longestPalindrome(s: str) -> str:
  # brute force
    maxSize = [0, -1, -1]
    for i in range(len(s)-1):
        size, j, k = 0, i-1, i+1
        if s[i] is s[i+1]:
            if i < len(s) - 2: k = i + 2
            else: k = i + 1
            size = (k-1) - (j+1)
        else: k = i + 1
        while j >= 0 and k < len(s):
            print(s[j], s[k])
            if s[j] is s[k]:
                k = k + 1
                j = j - 1
                size = k - j
                if size > maxSize[0]: maxSize = [size, j, k]
            else:
                if s[j] is s[k-1]:
                    size = size + 1
                    k = k - 1
                    if size > maxSize[0]: maxSize = [size, j, k]
                else:
                    if size > maxSize[0]: maxSize = [size, j+1, k-1]
                break
    if maxSize[0] > 0:
            return s[maxSize[1]:maxSize[2]+1]
    else:
        return None

# print(longestPalindrome("1forgeeksskeegroffor99999999999999999"))
# print(longestPalindrome("2eekk91k"))
# print(longestPalindrome("babad"))
# print(longestPalindrome("cbbdad"))

def minimumNumberOfPages(pages, days):
    # Write your code here
    if (days < 1 or 
        days > 1000000000 or 
        len(pages) < 1 or 
        len (pages) or 
        len(pages > days)):
        return -1
    previousWasOk = False
    assumedDays = len(pages)
    from math import ceil
    minPages = ceil(sum(pages)/len(pages))
    preMinPages = minPages
    while True:
        for chapterPages in pages:
            if chapterPages < 1 or chapterPages > 100000:
                return -1
            if chapterPages > minPages:
                assumedDays = assumedDays + ceil((chapterPages-minPages)/minPages)
        if assumedDays <= days:
            preMinPages = minPages
            minPages = minPages - 1
            if not previousWasOk: previousWasOk = True
        else:
            if previousWasOk: return preMinPages
            minPages = minPages + 1
        assumedDays = len(pages)

# print(minimumNumberOfPages([8, 2, 4, 10, 1], 6))

# https://leetcode.com/problems/container-with-most-water/
def maxArea(height: list[int]) -> int:
  # brute force
  def SolA():
    maxArea = 0
    for i in range(len(height)):
      for j in range(i+1, len(height)):
        minNum = height[i] if (height[i] < height[j]) else height[j]
        area = minNum * (j - i)
        maxArea = area if area > maxArea else maxArea
    return maxArea
  # two pointers
  def SolB():
    i, j, maxArea = 0, len(height)-1, 0
    while i < len(height) and j > 0:
      minNum = height[i] if (height[i] < height[j]) else height[j]
      area = minNum * (j - i)
      maxArea = area if area > maxArea else maxArea
      if height[i] < height[j]: i+= 1
      else: j -= 1
    return maxArea

  return SolB()

# print(maxArea([1,8,6,2,5,4,8,3,7]))
# print(maxArea([1,3,1,4,10000,2,1,5,3,999]))

# https://leetcode.com/problems/roman-to-integer/
def romanToInt(s: str) -> int:
  roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
  dig = 0
  for i in range(len(s)-1):
    if roman[s[i]] < roman[s[i+1]]: dig -= roman[s[i]]
    else: dig += roman[s[i]]
  dig += roman[s[-1]]
  return dig

# print(romanToInt("XII"))

# https://leetcode.com/problems/longest-common-prefix/
def longestCommonPrefix(strs: list[str]) -> str:
  commonstr = ""
  var = [None]*len(strs)
  char = 0
  minLen = len(strs[0])
  for str in strs:
    if len(str) < minLen:
      minLen = len(str)
  while char < minLen:
    for i in range(len(strs)):
      var[i] = strs[i][char]
    if var.count(var[0]) == len(var):
      commonstr += var[0]
      var = [None]*len(strs)
      char += 1
    else:
      return commonstr
  return commonstr

# int(strs[i][char].encode('utf-8').hex(), base=16)

# print(longestCommonPrefix(["dog","racecar","car"]))
# print(longestCommonPrefix(["flower","flower","flow","flight"]))
# print(longestCommonPrefix(["fl","fl","fl","fl"]))

# https://leetcode.com/problems/3sum/
def threeSum(nums: list[int]) -> list[list[int]]:
  lNums = []
  nums.sort()
  for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i-1]: continue
    j = i +1
    k = len(nums)-1
    while j < k:
      total = nums[i] + nums[j] + nums[k]
      if total == 0:
        lNums.append([nums[i], nums[j], nums[k]])
        j += 1
        while nums[j] == nums[j-1] and j < k:
          j += 1
      elif total > 0:
        k -= 1
      else:
        j += 1
  return lNums

# print(threeSum([-1, 0, 2, 1, 0, 2, -1, -4]))
# print(threeSum([1, 2, -2, -1, 2]))
# print(threeSum([-5, -2, 2, -3, 0, 1, 2, -1, 4]))
# print(threeSum([0,1,1]))
# print(threeSum([0,0,0,0]))

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
def letterCombinations(digits: str) -> list[str]:
  keyboard = {"2": "abc","3": "def","4": "ghi","5": "jkl","6": "mno","7": "pqrs","8": "tuv","9": "wxyz"}

  if len(digits) == 0 or len(digits) > 4:
    return []
  if len(digits) == 1:
    return keyboard[digits[0]]

  combs = []
  diglist = list(digits)
  def findString(diglist, ostr) -> list[str]:
    mainKey = keyboard[diglist[0]]
    for i in range(len(mainKey)):
      str = ostr + mainKey[i]
      if len(diglist) > 1: findString(diglist[1:], str)
      else: combs.append(str)
    return combs

  mainKey = keyboard[diglist[0]]
  for i in range(len(mainKey)):
    findString(diglist[1:], mainKey[i])

  return combs

# print(letterCombinations("3476"))

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
  if not head or not head.next: return None

  current = head
  headLen = 1
  while current.next:
    headLen += 1
    current = current.next

  if n > headLen or headLen - n + 1 == 0: return None
  pointer = headLen - n + 1
  if pointer == 1: return head.next

  current = head
  previous = head
  while current:
    pointer -= 1
    if pointer == 0:
      previous.next = current.next
      current = None
    else:
      previous = current
      current = current.next
  return head

def createList(vals):
  node0 = ListNode(vals[0])
  res = node0
  for i in range(1, len(vals)):
    node = ListNode(vals[i])
    if i < len(vals):
      node0.next = node
      node0 = node
  return res

# head = createList([1, 2])
# head = removeNthFromEnd(head, 1)


# https://leetcode.com/problems/valid-parentheses/
def isValid(s: str) -> bool:
  parmap = {"(" : ")","{" : "}","[" : "]"}
  stack = []
  for i in s:
    if i in parmap:
      stack.append(i)
    if i in parmap.values():
      if not stack: return False
      open = stack.pop()
      if parmap[open] != i: return False

  if stack: return False
  return True

# print(isValid(")"))
# print(isValid("()[{}"))
# print(isValid("{sdad(sdad[jb])}"))


# https://leetcode.com/problems/merge-two-sorted-lists/
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
  if not list1 and not list2: return None
  if not list1: return list2
  if not list2: return list1

  node0 = None
  res = None
  current1 = None
  current2 = None

  if list1.val < list2.val:
    node0 = ListNode(list1.val)
    current1 = list1.next
    current2 = list2
  else:
    node0 = ListNode(list2.val)
    current1 = list1
    current2 = list2.next
  res = node0

  while current1 and current2:
    if current1.val < current2.val:
      newnode = ListNode(current1.val)
      node0.next = newnode
      node0 = newnode
      current1 = current1.next
    elif current2.val < current1.val:
      newnode = ListNode(current2.val)
      node0.next = newnode
      node0 = newnode
      current2 = current2.next
    elif current1.val == current2.val:
      newnode = ListNode(current1.val)
      node0.next = newnode
      node0 = newnode
      newnode = ListNode(current2.val)
      node0.next = newnode
      node0 = newnode
      current1 = current1.next
      current2 = current2.next

  while current1:
    newnode = ListNode(current1.val)
    node0.next = newnode
    node0 = newnode
    current1 = current1.next
  while current2:
    newnode = ListNode(current2.val)
    node0.next = newnode
    node0 = newnode
    current2 = current2.next

  return res

# list1 = createList([4])
# list2 = createList([0, 2, 5, 8, 10])
# mergeTwoLists(list1, list2)

# https://leetcode.com/problems/generate-parentheses/
def generateParenthesis(n: int) -> list[str]:
  def SolA():
    def findString(slist):
      newlist = []
      for str in slist:
        nopen = str.count("(")
        nclose = str.count(")")
        if nclose == n:
          newlist.append(str)
          continue
        elif nopen == nclose:
          str += "("
          newlist.append(str)
        elif nopen == n:
          str += ")"
          newlist.append(str)
        elif nopen < n:
          newlist.append(str + "(")
          newlist.append(str + ")")
      return newlist

    slist = ["("]
    i = 1
    while i < 2*n:
      slist = findString(slist)
      i += 1

    return slist

  def SolB():
    def findString(slist):
      newlist = []
      for st in slist:
        nopen = st.split(",")[1]
        nclose = st.split(",")[2]
        st = st.split(",")[0]
        if nclose == str(n):
          newlist.append(st + "," + nopen + "," +  nclose)
          continue
        elif int(nopen) == int(nclose):
          st += "("
          newopen = str(int(nopen) + 1)
          newlist.append(st + "," + str(newopen) + "," +  str(nclose))
        elif nopen == str(n):
          st += ")"
          newclose = str(int(nclose) + 1)
          newlist.append(st + "," + str(nopen) + "," +  str(newclose))
        elif nopen < str(n):
          newopen = str(int(nopen) + 1)
          newlist.append(st + "(" + "," + newopen + "," + nclose)
          newclose = str(int(nclose) + 1)
          newlist.append(st + ")" + "," + nopen + "," + newclose)
      return newlist

    if n == 1: return ["()"]
    slist = ["(, 1, 0"]
    i = 0
    while i < 2*n - 1:
      slist = findString(slist)
      i += 1
    newlist = []
    for st in slist:
      newlist.append(st.split(",")[0])

    return newlist

  SolA()

# (
  # ((, ()
    # (((, ((), ()(
      # (((), (()(, (()), ()((, ()(),
        # ((()), (()(), (())(, ()((), ()()(
          # ((())), (()()), (())(), ()(()), ()()()

# generateParenthesis(1)

# https://leetcode.com/problems/merge-k-sorted-lists/
def mergeKLists(lists: list[ListNode]) -> ListNode:
  def SolA():
    linkeds = []
    for list in lists:
      if list == []: continue
      linkeds.append(createList(list))
    newlist = None
    for i in range(len(linkeds)):
      if linkeds[i] == []: continue
      newlist = mergeTwoLists(newlist, linkeds[i])
    return newlist

  def SolB(lists):
    convList = []
    for i in range(len(lists)):
      current = lists[i]
      while current:
        convList.append(current.val)
        current = current.next
    if convList == []: return None
    convList.sort()
    return createList(convList)

  linkeds = []
  for list in lists:
    if list == []: continue
    linkeds.append(createList(list))
  if linkeds == []: return None

  return SolB(linkeds)

lists = [[1,4,5],[1,3,4],[2,6]]
lists = [[1,4,5],[1,3,4],[]]
lists = [[]]
mergeKLists(lists)
