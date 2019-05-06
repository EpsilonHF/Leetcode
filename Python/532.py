"""
Given an array of integers and an integer k, you need to find 
the number of unique k-diff pairs in the array. Here a k-diff 
pair is defined as an integer pair (i, j), where i and j are 
both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: 
There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the 
number of unique pairs.
"""

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        d = dict()
        for num in nums:
            d[num] = d.get(num, 0) + 1

        count = 0

        for key in d:
            if k == 0 and d.get(key, 0) > 1:
                count += 1
            elif k and key+k in d:
                count += 1

        return count
