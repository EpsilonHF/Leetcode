"""
Given an integer array with all positive numbers and no duplicates, 
find the number of possible combinations that add up to a positive 
integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        comb = [0] * (target + 1)
        comb[0] = 1
        for i in range(1, len(comb)):
            for num in nums:
                if i >= num:
                    comb[i] += comb[i-num]

        return comb[-1]
