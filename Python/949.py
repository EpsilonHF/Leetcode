"""
Given an array of 4 digits, return the largest 24 hour time that 
can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  
Starting from 00:00, a time is larger if more time has elapsed 
since midnight.

Return the answer as a string of length 5.  If no valid time can 
be made, return an empty string.

Example 1:

Input: [1,2,3,4]
Output: "23:41"
"""

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        k = sorted(list(itertools.permutations(A)), reverse = True)

        for i in k:
            a, b, c, d = i
            su = (a*10 + b)
            sd = (c*10 + d)

            if su < 24 and sd < 60:
                return  f"{a}{b}:{c}{d}"

        return ''
