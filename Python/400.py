"""
Find the nth digit of the infinite integer sequence 
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed 
integer (n < 231).

Example 1:

Input:
3

Output:
3
"""

class Solution:
    def findNthDigit(self, n: int) -> int:
        up = bit = 1
        num = 0

        while n > num + bit * up * 9:
            num += bit * up * 9
            bit += 1
            up *= 10

        pos = up + (n - num - 1) // bit
        i = (n - num) % bit
        s = str(pos)

        return int(s[i-1])
