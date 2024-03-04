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

LL = singlyLinkedList()
LL.push(11)
LL.push(4)
LL.push(8)
LL.push(14)
LL.push(23)
var = LL.get(4)
print(var.val)
LL.set(3, 200)
LL.remove(1)
# LL.unshift(2)
# val = LL.pop()
# LL.reverse()
print("e")
