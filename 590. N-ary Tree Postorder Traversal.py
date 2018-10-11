
# Given an n-ary tree, return the postorder traversal of its nodes' values.
# Return its postorder traversal as: [5,6,3,2,4,1].

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        res = []
        if root == None:
            return res

        for child in root.children:
            child_list = self.postorder(child)
            res.extend(child_list)
        res.append(root.val)

        return res