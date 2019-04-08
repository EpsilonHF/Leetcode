"""
Given a collection of distinct integers, return all possible 
permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[]]
        else:
            return [[n] + p
                    for i, n in enumerate(nums)
                    for p in self.permute(nums[:i]+nums[i+1:])]
