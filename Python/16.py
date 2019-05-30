"""
Given an array nums of n integers and an integer target, find 
three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each 
input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)-2):
            start, end = i+1, len(nums) - 1

            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if total < target:
                    start += 1
                elif total > target:
                    end -= 1
                else:
                    return total

                if abs(total - target) < abs(ret - target):
                    ret = total

        return ret
