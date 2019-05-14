"""
In a given integer array nums, there is always exactly one largest 
element.

Find whether the largest element in the array is at least twice as 
much as every other number in the array.

If it is, return the index of the largest element, otherwise 
return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 
6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, 
so we return 1.
"""

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ret = nums[0]
        index = 0

        for i, val in enumerate(nums):
            if val > ret:
                index = i
                ret = val

        for i, val in enumerate(nums):
            if val != ret and ret < 2 * val:
                return -1

        return index
