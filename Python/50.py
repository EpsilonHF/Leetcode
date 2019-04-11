"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            return 1/self.myPow(x, -n)
        elif n == 0:
            return 1
        elif n == 1:
            return x
        elif n % 2 == 1:
            return x * self.myPow(x, n - 1)
        else:
            return self.myPow(x * x, n // 2)
