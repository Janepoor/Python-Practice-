# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/


from queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val,node))

        while q.qsize()>0:

            curr.next = q.get()[1]
            curr=curr.next

            if curr.next:
                q.put((curr.next.val, curr.next))
        return dummy.next