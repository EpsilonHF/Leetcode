"""
Given an array containing n distinct numbers taken from 
0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums) * (len(nums) + 1) // 2
        for num in nums:
            res -= num

        return res
