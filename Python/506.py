"""
Given scores of N athletes, find their relative ranks and the 
people with the top three highest scores, who will be awarded 
medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: 
The first three athletes got the top three highest scores, so 
they got "Gold Medal", "Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative 
ranks according to their scores.
"""

class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        newnums = sorted(nums, reverse = True)
        d = dict()
        d[newnums[0]] = 'Gold Medal'
        if len(newnums) > 1:
            d[newnums[1]] = 'Silver Medal'
        if len(newnums) > 2:
            d[newnums[2]] = 'Bronze Medal'

        for i in range(3, len(nums)):
            d[newnums[i]] = str(i + 1)

        return [d[index] for index in nums]
