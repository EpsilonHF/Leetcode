"""
Given a non-empty array of non-negative integers nums, the 
degree of this array is defined as the maximum frequency of 
any one of its elements.

Your task is to find the smallest possible length of a (contiguous) 
subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 
2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
"""

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = dict()
        MAX, ret = 0, len(nums)
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = [1, i, i]
            else:
                d[num][0] += 1
                d[num][2] = i
            MAX = max(MAX, d[num][0])

        for num in d:
            if d[num][0] == MAX:
                ret = min(ret, d[num][2] - d[num][1] + 1)

        return ret
