"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return 
the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
"""

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while n > m:
            m >>= 1
            n >>= 1
            i += 1

        return n << i
