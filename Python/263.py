"""
Write a program to check whether a given number is an ugly 
number.

Ugly numbers are positive numbers whose prime factors only 
include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
"""

class Solution:
    def isUgly(self, num: int) -> bool:

        while num > 1:
            if num % 2 == 0:
                num //= 2
            elif num % 3 == 0:
                num //= 3
            elif num % 5 == 0:
                num //= 5
            else:
                return False

        return num == 1
