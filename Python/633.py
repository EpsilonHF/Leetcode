"""
Given a non-negative integer c, your task is to decide whether 
there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start, end = 0, int(c ** 0.5)

        while start <= end:
            num = start ** 2 + end ** 2
            if num == c:
                return True
            elif num > c:
                end -= 1
            else:
                start += 1

        return False
