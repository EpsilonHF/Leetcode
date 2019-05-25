"""
In a array A of size 2N, there are N+1 unique elements, and 
exactly one of these elements is repeated N times.

Return the element repeated N times.

Example 1:

Input: [1,2,3,3]
Output: 3
"""

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        vals = set()

        for num in A:
            if num not in vals:
                vals.add(num)
            else:
                return num
