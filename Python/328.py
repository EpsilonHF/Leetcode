"""
Given a singly linked list, group all odd nodes together 
followed by the even nodes. Please note here we are talking 
about the node number and not the value in the nodes.

You should try to do it in place. The program should run in 
O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        count = 0
        res = ptr = head
        while head.next:
            count += 1
            if count % 2 == 0:
                pnext = ptr.next
                hnext = head.next
                head.next, ptr.next, hnext.next = hnext.next, hnext, pnext
                ptr = ptr.next
            else:
                head = head.next

        return res
