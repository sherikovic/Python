# Binary Search Trees are:
# - ordered and sorted
# - no duplicates allowed
# - right subtree value should be higher than the parent's
# - left subtree value should be lower than the parent's
# - any operation takes O(logN)
# - you don't replace nodes
#
#
#                  15
#          10               20
#      8       12       18       25
#                16       19       30


class Node:
    def __init__(self, value) -> None:
        self.val = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if not self.root:
            self.root = newNode
        else:
            current = self.root
            while current:
                if value > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = newNode
                        return current
                elif value < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = newNode
                        return current

    # def find(self, value):
    #     if not self.root:
    #         return None
    #     current = self.root
    #     while True:
    #         if value == current.val:
    #             return current
    #         elif value > current.val:
    #             if current.right:
    #                 current = current.right
    #             else:
    #                 return None
    #         elif value < current.val:
    #             if current.left:
    #                 current = current.left
    #             else:
    #                 return None
    #     return None

    def find(self, value):
        if not self.root:
            return None

        def traverse(node):
            if value == node.val:
                return node
            elif value > node.val and node.right:
                self.parent = node
                return traverse(node.right)
            elif value < node.val and node.left:
                self.parent = node
                return traverse(node.left)
            else: return None

        self.parent = None
        return traverse(self.root), self.parent

    def delete(self, node):
        node, parent = self.find(node)
        # node has no children
        if not node.right and not node.left:
            if parent.right == node.val:
                parent.right = None
            else:
                parent.left = None
        # node has one child
        elif node.right and not node.left:
            toBeReplaced = node.right
            if node.val > parent.val:
                parent.right = toBeReplaced
            else:
                parent.left = toBeReplaced
            del node
        elif not node.right and node.left:
            toBeReplaced = node.left
            if node.val > parent.val:
                parent.right = toBeReplaced
            else:
                parent.left = toBeReplaced
            del node
        return tree


def createATree(nums):
    tree = BinarySearchTree()
    for num in nums:
        tree.insert(num)
    return tree


#                   14
#          10               20
#      5       12       17       89
#    2            13               100
nums = [14, 10, 20, 5, 12, 17, 89, 2, 13, 100]
tree = createATree(nums)
node, parent = tree.find(5)
# tree = tree.delete(89)
print(node.val, parent.val)
