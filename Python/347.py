"""
Given a non-empty array of integers, return the k most frequent 
elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()

        for num in nums:
            d[num] = d.get(num, 0) + 1

        d = sorted(d, key = lambda x: d[x], reverse = True)

        return d[:k]
