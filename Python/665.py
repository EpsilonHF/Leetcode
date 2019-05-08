"""
Given an array with n integers, your task is to check if it 
could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] 
holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: 
You could modify the first 4 to 1 to get a non-decreasing array.
"""

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        dec1 = dec2 = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                dec1 += 1

        for i in range(2, len(nums)):
            if nums[i] < nums[i-2]:
                dec2 += 1

        return dec1 < 2 and dec2 < 2
