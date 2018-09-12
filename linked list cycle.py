# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/

# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        fast = head.next
        slow = head

        while fast != slow:
            if fast == None or fast.next == None:
                return False
            fast = fast.next.next
            slow = slow.next

        return True