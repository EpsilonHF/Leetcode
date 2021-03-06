"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        node1 = less = ListNode(0)
        less.next = head
        node2 = greater = ListNode(0)
        greater.next = head

        while head:
            if head.val >= x:
                greater.next = head
                greater = head

            else:
                less.next = head
                less = head

            head = head.next

        greater.next = None
        less.next = node2.next

        return node1.next
