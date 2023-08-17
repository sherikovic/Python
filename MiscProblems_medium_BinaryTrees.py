class Node:
    def __init__(self, value) -> None:
        self.val = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if not self.root:
            self.root = newNode
            return self
        else:
            # initialize a queue
            queue = []
            queue.append(self.root)

            while queue:
                current = queue.pop(0)
                if not current.left:
                    current.left = newNode
                    return self
                elif not current.right:
                    current.right = newNode
                    return self
                else:
                    queue.append(current.left)
                    queue.append(current.right)


def createATree(nums):
    tree = BinaryTree()
    for num in nums:
        tree.insert(num)
    return tree


# Check if two binary trees are identical or not
# binary trees are identical when they have the same structure and contents
# x, y are nodes of each tree
def areIdentical(x, y):
    from collections import deque

    if not x and not y:
        return True
    if not x or not y:
        return False

    # queueX = []
    # queueY = []
    # queueX.append(x)
    # queueY.append(y)
    stack = deque()
    stack.append((x, y))

    # while queueX and queueY:
    while stack:
        # x, y = queueX.pop(), queueY.pop()
        x, y = stack.pop()
        if x.val != y.val:
            return "Not identical"

        if x.left and y.left:
            stack.append((x.left, y.left))
            # queueX.append(x.left)
            # queueY.append(y.left)
        elif x.left or y.left:
            return "Not identical"

        if x.right and y.right:
            stack.append((x.right, y.right))
            # queueX.append(x.right)
            # queueY.append(y.right)
        elif x.right or y.right:
            return "Not identical"

    return "Identical"


# nums1 = [4, 10, 20, 5, 12, 89, 45, 23]
# nums2 = [4, 10, 20, 5, 12, 89, 23, 45]
# tree1 = createATree(nums1)
# tree2 = createATree(nums2)
# print(areIdentical(tree1.root, tree2.root))
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# Calculate the height of a binary tree
# The height or depth of a binary tree is the total number of
# edges or nodes on the longest path from the root node to the leaf node
# Solution A
def calculateBinaryTreeHeight(tree):
    if not tree.root:
        return None

    queue = []
    queue.append(tree.root)
    depth = 0

    while queue:
        nodesInQueue = len(queue)
        while nodesInQueue:
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            nodesInQueue -= 1
        depth += 1

    return depth


# Solution B:
def maxDepth(node):
    if not node:
        return 0
    return 1 + max(maxDepth(node.left), maxDepth(node.right))


# nums = [4, 10, 20, 5, 12, 89, 45, 23]
# tree = createATree(nums)
# print(calculateBinaryTreeHeight(tree))
# print(maxDepth(tree.root))
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# Delete a binary tree
def deleteBinaryTree(node):
    if not node:
        return None

    if node.left:
        deleteBinaryTree(node.left)
    if node.right:
        deleteBinaryTree(node.right)
    node = None


# nums = [4, 10, 20, 5, 12, 89, 45, 23]
# tree = createATree(nums)
# tree = deleteBinaryTree(tree.root)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
