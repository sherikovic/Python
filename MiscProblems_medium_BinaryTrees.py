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

    # traverse a tree in an inorder fashion - DepthFirst
    # depth of the node on the left
    # the node
    # depth of the node on the right
    def inOrderDFSTraverse(self):
        if not self.root:
            return None

        queue = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            queue.append(node)
            if node.right:
                traverse(node.right)

        traverse(self.root)
        return queue

    # traverse a tree in a preorder fashion - DepthFirst
    # the node
    # depth of the node on the left
    # depth of the node on the right
    def preOrderDFSTraverse(self):
        if not self.root:
            return None

        queue = []
        def traverse(node):
            queue.append(node)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(self.root)
        return queue

    # traverse a tree in a postorder fashion - DepthFirst
    # depth of the node on the left
    # depth of the node on the right
    # the node
    def postOrderDFSTraverse(self):
        if not self.root:
            return None

        queue = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            queue.append(node)

        traverse(self.root)
        return queue

    def levelOrderBFSTraverse(self):
        if not self.root:
            return None

        data = [self.root]
        queue = [self.root]
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

    def reverseLevelOrderBFSTraverse(self):
        if not self.root:
            return None

        from collections import deque
        queue = []
        stack = deque()
        queue.append(self.root)  # will be the first one to pop
        stack.append(self.root)  # will be the last one to pop

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

    def isValidBinaryTree(self):
        if not self.root:
            return "Not even a tree!"

        queue = [self.root]
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

    def calculateBinaryTreeHeight(self):
        if not self.root:
            return None

        queue = []
        queue.append(self.root)
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

    def maxDepth(self, node):
        if not node:
            return 0
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))

    def deleteTree(self, node):
        if not node:
            return None
        if node.left:
            self.deleteBinaryTree(node.left)
        if node.right:
            self.deleteBinaryTree(node.right)
        node = None


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

#                   4
#          10               20
#      5       12       89       45
#   23   32
# nums = [4, 10, 20, 5, 12, 89, 45, 23, 32]
# tree = createATree(nums)

# Q = inOrderDFSTreeTraversal(tree)
# Q = preOrderDFSTreeTraversal(tree)
# Q = postOrderDFSTreeTraversal(tree)
# Q = levelOrderBFSTreeTraversal(tree)
# Q = reverseLevelOrderBFSTreeTraversal(tree)

# while Q:
#     print(Q.pop().val, end=" ")
# for q in Q:
#     print(q.val, end=" ")

# self.maxDepth(tree.root)
# tree.root.left.left.right = None
# tree.root.left.right.left = None
# print(tree.isValidBinaryTree())
# print(self.deleteBinaryTree(tree.root)) # should be none