# Binary Trees are:
# - unordered
# - duplicates are allowed
# - any operation takes O(N)
# - insertion is as follows:
#   - insert in left if left is empty
#   - otherwise insert in right
#
#
#                  1
#          2               3
#      4       5       6       7
#    8               9   10
#
# Traversal techniques (this is not realistic because left is still empty):
# - In-Order: 8 4 2 5 1 9 6 10 3 7
# - Pre-Order: 1 2 4 8 5 3 6 9 10 7
# - Post-Order: 8 4 5 2 9 10 6 7 3 1
# - Level-Order: 1 2 3 4 5 6 7 8 9 10


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
            queue = [self.root]

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


# traverse a tree in an inorder fashion - DepthFirst
# depth of the node on the left
# the node
# depth of the node on the right
def inOrderDFSTreeTraversal(tree):
    if not tree.root:
        return None
    queue = []

    def traverse(node):
        if node.left:
            traverse(node.left)
        queue.append(node)
        if node.right:
            traverse(node.right)

    traverse(tree.root)
    return queue


#                   4
#          10               20
#      5       12       89       45
#   23   32
# nums = [4, 10, 20, 5, 12, 89, 45, 23, 32]
# tree = createATree(nums)
# Q = inOrderDFSTreeTraversal(tree)
# for q in Q:
#     print(q.val, end=" ")
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# traverse a tree in a preorder fashion - DepthFirst
# the node
# depth of the node on the left
# depth of the node on the right
def preOrderDFSTreeTraversal(tree):
    if not tree.root:
        return None
    queue = []

    def traverse(node):
        queue.append(node)
        if node.left:
            traverse(node.left)
        if node.right:
            traverse(node.right)

    traverse(tree.root)
    return queue


#                   4
#          10               20
#      5       12       89       45
#   23   32
# nums = [4, 10, 20, 5, 12, 89, 45, 23, 32]
# tree = createATree(nums)
# Q = preOrderDFSTreeTraversal(tree)
# for q in Q:
#     print(q.val, end=" ")
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# traverse a tree in a postorder fashion - DepthFirst
# depth of the node on the left
# depth of the node on the right
# the node
def postOrderDFSTreeTraversal(tree):
    if not tree.root:
        return None
    queue = []

    def traverse(node):
        if node.left:
            traverse(node.left)
        if node.right:
            traverse(node.right)
        queue.append(node)

    traverse(tree.root)
    return queue


#                   4
#          10               20
#      5       12       89       45
#   23   32
# nums = [4, 10, 20, 5, 12, 89, 45, 23, 32]
# tree = createATree(nums)
# Q = postOrderDFSTreeTraversal(tree)
# for q in Q:
#     print(q.val, end=" ")
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# traverse a tree in a level order fashion - BreadthFirst
def levelOrderBFSTreeTraversal(tree):
    if not tree.root:
        return None
    data = [tree.root]
    queue = [tree.root]
    while queue:
        nodesInQueue = len(queue)
        while nodesInQueue:
            current = queue.pop(0)
            if current.left:
                data.append(current.left)
                queue.append(current.left)
            if current.right:
                data.append(current.right)
                queue.append(current.right)
            nodesInQueue -= 1
    return data


#                   4
#          10               20
#      5       12       89       45
#   23   32
# nums = [4, 10, 20, 5, 12, 89, 45, 23, 32]
# tree = createATree(nums)
# Q = levelOrderBFSTreeTraversal(tree)
# for q in Q:
#     print(q.val, end=" ")
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# traverse a tree in a reverse level order
def reverseLevelOrderBFSTreeTraversal(tree):
    from collections import deque

    if not tree.root:
        return None
    queue = []
    stack = deque()
    queue.append(tree.root)  # will be the first one to pop
    stack.append(tree.root)  # will be the last one to pop

    while queue:
        nodesInQueue = len(queue)
        while nodesInQueue:
            current = queue.pop(0)
            current = queue.pop(nodesInQueue - 1)
            if current.right:
                queue.append(current.right)
                stack.append(current.right)
            if current.left:
                queue.append(current.left)
                stack.append(current.left)
            nodesInQueue -= 1
    return stack


#                   4
#          10               20
#      5       12       89       45
#   23   32
# nums = [4, 10, 20, 5, 12, 89, 45, 23, 32]
# tree = createATree(nums)
# S = reverseLevelOrderBFSTreeTraversal(tree)
# while S:
#     print(S.pop().val, end=" ")
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# check if the given tree is a complete binary tree
def checkIfBinaryTree(tree):
    if not tree.root:
        return "Not even a tree!"

    queue = [tree.root]
    flag = False
    while queue:
        current = queue.pop(0)
        if current.left and current.right:
            if flag:
                return "Not a complete binary tree!"
            else:
                queue.append(current.left)
            queue.append(current.right)
        elif current.left and not current.right:
            if flag:
                return "Not a complete binary tree!"
            else:
                flag = True
                queue.append(current.left)
        elif not current.left and current.right:
            return "Not a complete binary tree!"
    return "Yes it is a tree!"


#                   4
#          10               20
#      5       12       89       45
#   23  32   44  21
# nums = [4, 10, 20, 5, 12, 89, 45, 23, 32, 44, 21]
# tree = createATree(nums)
# tree.root.left.left.right = None
# tree.root.left.right.left = None
# print(checkIfBinaryTree(tree))
