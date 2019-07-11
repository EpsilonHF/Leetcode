"""
Given a linked list, rotate the list to the right by k places, where 
k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        if len(nums) == 0:
            return None

        k = k % len(nums)
        nums = nums[-k:] + nums[:-k]

        head = ptr = ListNode(nums[0])

        for num in nums[1:]:
            node = ListNode(num)
            head.next = node
            head = node

        return ptr
