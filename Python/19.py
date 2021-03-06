"""
Given a linked list, remove the n-th node from the end of 
list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list 
becomes 1->2->3->5.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        runner = slower = head
        for i in range(n):
            runner = runner.next
        if runner is None:
            head = head.next
            return head

        while runner.next:
            runner = runner.next
            slower = slower.next
        slower.next = slower.next.next

        return head
