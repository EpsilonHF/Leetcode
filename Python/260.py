"""
Given an array of numbers nums, in which exactly two elements 
appear only once and all the other elements appear exactly 
twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        for num in nums:
            res ^= num

        res1 = res2 = 0

        bit = res & ~(res-1)
        for num in nums:
            if num & bit:
                res1 ^= num
            else:
                res2 ^= num

        return [res1, res2]
