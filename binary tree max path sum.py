# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    max_sum = -(1 << 31)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)

        return self.max_sum

    def helper(self, root):
        if root == None:
            return 0

        left = max(0, self.helper(root.left))
        right = max(0, self.helper(root.right))

        self.max_sum = max(self.max_sum, left + right + root.val)

        return max(left, right) + root.val
