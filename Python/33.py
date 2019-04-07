"""
Suppose an array sorted in ascending order is rotated at some 
pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array 
return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, H = 0, len(nums)
        while L < H:
            M = (L+H) // 2
            if target < nums[0] < nums[M]:
                L = M+1
            elif target >= nums[0] > nums[M]:
                H = M
            elif nums[M] < target:
                L = M+1
            elif nums[M] > target:
                H = M
            else:
                return M
        return -1
