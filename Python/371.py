"""
Calculate the sum of two integers a and b, but you are not 
allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:

        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        mask = 0xFFFFFFFF

        while b != 0:

            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        return a if a <= MAX else ~(a ^ mask)
