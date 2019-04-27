"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()
        for num in nums1:
            d[num] = d.get(num, 0) + 1

        res = []
        for num in nums2:
            if d.get(num, 0) > 0:
                res.append(num)
            d[num] = d.get(num, 0) - 1

        return res
