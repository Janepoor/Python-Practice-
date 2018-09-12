# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # using a hashmap to store the random one
        if head == None:
            return head

        # phase 1 copy all the node
        node = head
        hash = {}
        while node:
            hash[node] = RandomListNode(node.label)
            node = node.next


        # phase2 copy all the next and the random

        node = head
        while node != None:
            hash[node].next = hash.get(node.next)
            hash[node].random = hash.get(node.random)
            node = node.next

        return hash[head]