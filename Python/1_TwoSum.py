"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        all_nums = dict()
        for i in range(len(nums)):
            if target - nums[i] in all_nums:
                return [all_nums[target-nums[i]], i]
            all_nums[nums[i]] = i
