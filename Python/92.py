"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        start = node = ListNode(0)
        node.next = head
        pos = 0

        while pos < m - 1:
            node = node.next
            pos += 1

        node1 = node
        node = node.next
        pos += 1
        node2 = node

        post = node.next
        while pos < n:
            pos += 1
            pre = node
            node, post = post, post.next
            node.next = pre

        node1.next = node
        node2.next = post

        return start.next