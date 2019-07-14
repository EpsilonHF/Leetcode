"""
Suppose an array sorted in ascending order is rotated at some pivot 
unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            if nums[low] < nums[high]:
                return nums[low]
            mid = (low + high) // 2
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid

        return nums[low]
