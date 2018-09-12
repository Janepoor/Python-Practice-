
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #         newhead = None
        #         while head != None:
        #             tmp = head.next
        #             head.next = newhead
        #             newhead = head
        #             head = tmp
        #         return newhead

        if head == None or head.next == None:
            return head

        root = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return root

#         newhead = None
#         while head != None:
#             next = head.next
#             head.next = newhead
#             newhead= head
#             head = next
#         return newhead
