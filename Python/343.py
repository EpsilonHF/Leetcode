"""
Given a positive integer n, break it into the sum of at least 
two positive integers and maximize the product of those integers. 
Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4: return n - 1
        if n == 4: return 4
        p3 = n // 3
        if n % 3 == 2:
            p2 = 1
        elif n % 3 == 1:
            p2 = 2
            p3 -= 1
        else:
            p2 = 0

        return (2**p2) * (3**p3)
