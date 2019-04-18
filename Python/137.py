"""
Given a non-empty array of integers, every element appears 
three times except for one, which appears exactly once. 
Find that single one.

Note:

Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = two = 0
        for i in nums:
            one = (one ^ i) & ~two
            two = (two ^ i) & ~one

        return one

