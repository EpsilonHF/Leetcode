"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre, ptr = head, head.next

        while ptr:
            if ptr.val == pre.val:
                ptr = ptr.next
            else:
                pre.next = ptr
                pre = ptr
                ptr = ptr.next
        pre.next = None

        return head
