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
        if self.length == 0: self.head = None
        return current
    def shift(self):
        if not self.head: return None
        currentHead = self.head
        self.head = currentHead.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return currentHead
    

print(hash("hello"))