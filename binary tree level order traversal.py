# 102. Binary Tree Level Order Traversal

# https://leetcode.com/problems/binary-tree-level-order-traversal/description/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        res = []
        level = [root]

        while level:
            res.append([node.val for node in level])

            temp = []
            for n in level:
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)

            level = temp

        return res
