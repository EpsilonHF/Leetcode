"""
Given a set of distinct integers, nums, return all possible 
subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        else:
            return [[nums[0]] + lst for lst in self.subsets(nums[1:])] +\
                   self.subsets(nums[1:])