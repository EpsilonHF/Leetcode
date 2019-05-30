"""
Find the kth largest element in an unsorted array. Note that it 
is the kth largest element in the sorted order, not the kth distinct 
element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
"""

from random import randint
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        index = randint(0, len(nums)-1)
        nums[index], nums[0] = nums[0], nums[index]
        key = nums[0]
        pos = 1
        i = 1

        while i < len(nums):
            if nums[i] > key:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
            i += 1

        if pos == k:
            return key

        elif pos > k:
            return self.findKthLargest(nums[1: pos], k)

        else:
            return self.findKthLargest(nums[pos:], k - pos)
