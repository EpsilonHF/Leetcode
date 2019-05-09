"""
Given an array consisting of n integers, find the contiguous 
subarray of given length k that has the maximum average value. 
And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = ret = sum(nums[:k])

        for i in range(k, len(nums)):
            total = total + nums[i] - nums[i - k]
            ret = max(ret, total)

        return ret/k