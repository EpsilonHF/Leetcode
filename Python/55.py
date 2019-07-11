"""
Given an array of non-negative integers, you are initially positioned 
at the first index of the array.

Each element in the array represents your maximum jump length at that 
position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True

        pos = len(nums) - 2
        count = 0
        while pos > 0:
            if nums[pos] > count:
                count = 0
            else:
                count += 1
            pos -= 1

        return nums[0] > count
