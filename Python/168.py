"""
Given a positive integer, return its corresponding column 
title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
"""

class Solution:
    def convertToTitle(self, n: int) -> str:
        str = ''

        while n:
            str += chr((n-1)%26 + ord('A'))
            n = (n-1)//26

        return str[::-1]
