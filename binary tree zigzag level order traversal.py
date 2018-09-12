
class TreeNode(object):
    def __init__(self,x):
        self.val  = x
        self.right = None
        self.left = None

#leetcode 103
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

def zigzagLevelOrder(root):

    if not root:
        return []
    res = []
    level = [root]
    count = 0

    while level:
        if count %2 == 0:
            res.append([node.val for node in level])
        else:
            res.append([node.val for node in level[::-1]])
        temp = []
        for node in level:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        level = temp
        count += 1

    return res