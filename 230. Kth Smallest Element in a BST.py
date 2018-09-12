# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# just do a inorder travesal and store all the first k elements
class Solution(object):
    def kthSmallest(self, root, k):
        count = []
        self.helper(root, count)
        return count[k - 1]

    def helper(self, node, count):
        if not node:
            return
        self.helper(node.left, count)
        count.append(node.val)
        self.helper(node.right, count)
