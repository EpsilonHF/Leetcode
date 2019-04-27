"""
Given an integer (signed 32 bits), write a function to check 
whether it is a power of 4.

Example 1:

Input: 16
Output: true
"""

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num > 1:
            if num % 4:
                return False
            num >>= 2
        
        return num == 1
