
# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not preorder: return None

        root = TreeNode(preorder[0])
        root_pos = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1: 1 + root_pos], inorder[: root_pos])
        root.right = self.buildTree(preorder[root_pos + 1:], inorder[root_pos + 1:])

        return root