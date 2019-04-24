"""
Given an array nums of n integers where n > 1,  return an 
array output such that output[i] is equal to the product of 
all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        p = 1

        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]

        for i in range(len(nums)-1, -1, -1):
            ans[i] *= p
            p *= nums[i]

        return ans
