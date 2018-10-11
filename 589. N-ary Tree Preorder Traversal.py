# Given an n-ary tree, return the preorder traversal of its nodes' values.



"""
# Definition for a Node.
"""

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


# so the preorder is

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res

        res.append(root.val)
        for child in root.children:
            child_res = self.preorder(child)
            res.extend(child_res)

        return res
