"""
Given an integer array, find three numbers whose product is 
maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        max1 = nums[-1] * nums[-2] * nums[-3]
        max2 = nums[0] * nums[1] * nums[-1]

        return max(max1, max2)
