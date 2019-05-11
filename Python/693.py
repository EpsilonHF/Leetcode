"""
Given a positive integer, check whether it has alternating bits: 
namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
"""

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        pre = n & 1

        while n:
            n >>= 1
            if not pre ^ (n & 1):
                return False
            pre = 1 - pre

        return True
