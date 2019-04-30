"""
Given two non-negative integers num1 and num2 represented as 
string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert 
the inputs to integer directly.
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        carry = 0
        ans = ""

        while l1 or l2:
            if l1:
                x1 = int(num1[l1-1])
                l1 -= 1
            else:
                x1 = 0
            if l2:
                x2 = int(num2[l2-1])
                l2 -= 1
            else:
                x2 = 0
            ans += str((x1 + x2 + carry) % 10)
            carry = (x1 + x2 + carry) // 10

        if carry:
            ans += '1'

        return ans[::-1]
