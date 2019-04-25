"""
Given an array nums containing n + 1 integers where each 
integer is between 1 and n (inclusive), prove that at least 
one duplicate number must exist. Assume that there is only 
one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)
