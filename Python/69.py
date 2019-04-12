"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed 
to be a non-negative integer.

Since the return type is an integer, the decimal digits are 
truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        n = x//2 + 1

        while True:
            n = (x + n**2) //(2*n)
            if n**2 <= x and (n+1)**2 > x:
                
                return n
