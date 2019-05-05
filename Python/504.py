"""
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ""
        n = abs(num)

        while n >= 7:
            ans += str(n % 7)
            n //= 7
        ans += str(n)

        if num >= 0:
            return ans[::-1]
        else:
            return '-' + ans[::-1]
