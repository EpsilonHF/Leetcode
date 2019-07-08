"""
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        nums = sorted(candidates)

        def dfs(num, pre, index):
            if num < 0:
                return
            if num == 0:
                ans.append(pre)
                return

            for i in range(index, len(nums)):
                if nums[i] > num:
                    break
                if i > index and nums[i] == nums[i-1]:
                    continue
                dfs(num - nums[i], pre + [nums[i]], i+1)

        dfs(target, [], 0)

        return ans
