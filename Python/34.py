"""
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if not len(nums):
            return ans

        start, end = 0, len(nums)-1
        while start < end:
            mid = (start+end)//2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid

        if nums[end] != target:
            return ans
        ans[0] = end

        start, end = 0, len(nums)-1
        while start < end:
            mid = (start + end)//2+1
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid
        ans[1] = end

        return ans
