"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        return nums == nums[::-1]
