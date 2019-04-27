"""
Your task is to calculate ab mod 1337 where a is a positive 
integer and b is an extremely large positive integer given in 
the form of an array.

Example 1:

Input: a = 2, b = [3]
Output: 8
"""

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        div = 1337
        res = 1
        level = a % div

        for num in b[::-1]:
            res = (res * (level ** num)) % div
            level = (level ** 10) % div

        return res % div
