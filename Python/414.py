"""
Given a non-empty array of integers, return the third maximum 
number in this array. If it does not exist, return the maximum 
number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        res = [float('-inf')] * 3

        for num in set(nums):
            if num > res[0]:
                res = [num, res[0], res[1]]
            elif num > res[1]:
                res = [res[0], num, res[1]]
            elif num > res[2]:
                res = [res[0], res[1], num]

        if res[2] > float('-inf'):
            return res[2]
        else:
            return res[0]
