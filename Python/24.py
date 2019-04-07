"""
Given a linked list, swap every two adjacent nodes and return 
its head.

You may not modify the values in the list's nodes, only nodes 
itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ptr = head
        pre = ListNode(None)
        pre.next = ptr
        res = pre

        while ptr and ptr.next:
            a = ptr.next
            pre.next, ptr.next, a.next = a, a.next, ptr
            pre = ptr
            ptr = ptr.next

        return res.next
