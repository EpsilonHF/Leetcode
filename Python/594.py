"""
We define a harmonious array is an array where the difference 
between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its 
longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
"""

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            d[num] = d.get(num, 0) + 1

        ret = 0
        for num in d:
            if d.get(num + 1, 0):
                ret = max(ret, d[num] + d[num + 1])

        return ret
