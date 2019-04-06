"""
Given a 32-bit signed integer, reverse digits of an integer.
"""

class Solution:
    def reverse(self, x: int) -> int:
        flag = -1 if x < 0 else 1
        x = str(x*flag)[::-1]
        x = int(x)

        if x > 2147483647: return 0
        return x*flag
