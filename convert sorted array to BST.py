# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == None:
            return None
        return self.buildtree(nums, 0, len(nums) - 1)

    def buildtree(self, nums, start, end):
        if start > end:
            return None
        node = TreeNode(nums[(start + end) / 2])
        node.left = self.buildtree(nums, start, (start + end) / 2 - 1)
        node.right = self.buildtree(nums, (start + end) / 2 + 1, end)
        return node