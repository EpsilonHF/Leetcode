"""
Given an integer, write a function to determine if it is a 
power of three.

Example 1:

Input: 27
Output: true
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            if n % 3:
                return False
            n //= 3

        return n == 1
