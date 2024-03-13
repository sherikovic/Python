# 11 -> 4 -> 8 -> 23
# head ---------> tail
# push: adds a new tail ie 23 -> 45 (new tail)
# pop: retrieves the current tail (23, new tail becomes 8)
# shift: shifts the current head (11 is removed and 4 is the new head)
# unshift: adds a new head (2 -> 11 -> 4 -> 8 -> 23)

# insertion O(1)
# removal O(1) or O(N)
# searching, accessing O(N)

class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None

class singlyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    def get(self, index):
        if index < 0 or index >= self.length: return None
        i = 0
        current = self.head
        while i < index:
            current = current.next
            i += 1
        return current
    def set(self, index, val):
        if index < 0 or index >= self.length: return None
        nodeToBeUpdated = self.get(index)
        if nodeToBeUpdated:
            nodeToBeUpdated.val = val
            return True
        else:
            return False
    def insert(self, val, index): # there has to be a list to insert in
        if index < 0 or index >= self.length: return None
        if index == 0: return self.unshift(val)
        nodeBeforeToBeAdded = self.get(index-1)
        nodeAfterToBeAdded = nodeBeforeToBeAdded.next
        newNode = Node(val)
        nodeBeforeToBeAdded.next = newNode
        newNode.next = nodeAfterToBeAdded
        self.length += 1
        return newNode
    def sortedInsert(self, val): # insert in an already sorted list
        if not self.head:
            self.head = Node(val)
            self.length += 1
            return self.head
        if val < self.head.val:
            return self.unshift(val)
        current = self.head
        index = 0
        while current.next:
            index += 1
            if val > current.next.val:
                current = current.next
            elif val < current.next.val:
                return self.insert(val, index)
    def push(self, val):
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self
    def pop(self):
        if not self.head: return None
        prev = None
        current = self.head
        while current.next:
            prev = current
            current = current.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0: self.head =None
        return current
    def shift(self):
        if not self.head: return None
        currentHead = self.head
        self.head = currentHead.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return currentHead
    def unshift(self, val):
        if not self.head: return None
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        return self
    def remove(self, index):
        if index < 0 or index >= self.length: return None
        if index == 0: return self.shift()
        if index == self.length - 1: return self.pop()
        prevToBeDeleted = self.get(index-1)
        prevToBeDeleted.next = prevToBeDeleted.next.next
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        current = self.tail
        next = current.next
        while next:
            temp = next.next
            next.next = current
            current = next
            next = temp
        self.tail.next = None
        return self
    def sort(self):
        if not self.head: return None
        orderedList = singlyLinkedList()
        current = self.head
        while current:
            orderedList.sortedInsert(current.val)
            current = current.next
        return orderedList
    def printList(self):
        ptr = self.head
        while ptr:
            if ptr.next:
                print(ptr.val, end=" -> ")
            else:
                print(ptr.val)
            ptr = ptr.next


def mergeTwoLOrderedists(L1, L2):
    mergedList = singlyLinkedList()
    pointer1 = L1.head
    pointer2 = L2.head
    if pointer1.val < pointer2.val:
        mergedList.push(pointer1.val)
        pointer1 = pointer1.next
    else:
        mergedList.push(pointer2.val)
        pointer2 = pointer2.next
    while pointer1 and pointer2:
        if pointer1.val < pointer2.val:
            mergedList.push(pointer1.val)
            pointer1 = pointer1.next
        else:
            mergedList.push(pointer2.val)
            pointer2 = pointer2.next
    while pointer1:
        mergedList.push(pointer1.val)
        pointer1 = pointer1.next
    while pointer2:
        mergedList.push(pointer2.val)
        pointer2 = pointer2.next
    mergedList.printList()
    return mergedList


L1 = singlyLinkedList()
L2 = singlyLinkedList()
for i in [1, 3, 5, 7, 9]: L1.push(i)
for i in [1, 2, 4, 6, 10, 23]: L2.push(i)
L1.sort()
L2.sort()
mergeTwoLOrderedists(L1, L2)



############## reverse ##############
# 11 -> 4 -> 8 -> 14 -> 23
# 11 <- 4 <- 8 <- 14 <- 23

# temp = self.head 11
# self.head = self.tail 23
# self.tail = temp 11

# current 11
# next = 4

# temp = 4.next = 8
# 4.next = 11
# current = next = 4
# next = 8

# temp = 8.next = 14
# 8.next = 4
# current = next = 8
# next = 14

# temp = 14.next = 23
# 14.next = 8
# current = 14
# next = 23

# temp = 23.next = none
# 23.next = 14
# current = 23
# next = none

# LL = singlyLinkedList()
# LL.push(11)
# LL.push(4)
# LL.push(8)
# LL.push(14)
# LL.push(23)
# var = LL.get(4)
# print(var.val)
# LL.set(3, 200)
# LL.printList()
# LL.remove(1)
# LL.unshift(2)
# val = LL.pop()
# LL.reverse()
# LL.insert(33, 2)
# LL.printList()
# OLL = LL.sort()
# OLL.printList()
