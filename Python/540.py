"""
Given a sorted array consisting of only integers where every element appears 
exactly twice except for one element which appears exactly once. Find this 
single element that appears only once.

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
"""


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right-left)//2
            nei = mid+1 if mid%2 == 0 else mid-1

            if nums[mid] == nums[nei]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
