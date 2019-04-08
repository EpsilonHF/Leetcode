"""
Given a sorted array and a target value, return the index 
if the target is found. If not, return the index where it 
would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)
        if nums[-1] < target: return len(nums)

        while start < end:
            mid = (start+end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target and nums[mid+1] > target:
                return mid + 1
            elif nums[mid] > target:
                end = mid
            else:
                start = mid + 1

        return mid
