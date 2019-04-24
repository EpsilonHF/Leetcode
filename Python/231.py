"""
Given an integer, write a function to determine if it is a 
power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n:
            if n == 1:
                return True
            elif n % 2:
                return False
            else:
                n /= 2

        return False
