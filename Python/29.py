"""
Given two integers dividend and divisor, divide two integers 
without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        a = abs(dividend)
        b = abs(divisor)
        ret = 0

        for i in range(31, -1, -1):
            if (a >> i) - b >= 0:
                ret += 1 << i
                a -= b << i

        return ret if dividend * divisor > 0 else -ret
