"""
Given a positive integer, output its complement number. The 
complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 
32-bit signed integer.
You could assume no leading zero bit in the integer’s binary 
representation.
Example 1:
Input: 5
Output: 2
Explanation: 
The binary representation of 5 is 101 (no leading zero bits), 
and its complement is 010. So you need to output 2.
"""

class Solution:
    def findComplement(self, num: int) -> int:
        n = 1
        while n <= num:
            n <<= 1

        return n - 1 - num
