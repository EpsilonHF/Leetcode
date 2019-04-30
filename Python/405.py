"""
Given an integer, write an algorithm to convert it to hexadecimal. 
For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. 
If the number is zero, it is represented by a single zero 
character '0'; otherwise, the first character in the hexadecimal 
string will not be the zero character.
The given number is guaranteed to fit within the range of a 
32-bit signed integer.
You must not use any method provided by the library which 
converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
"""

class Solution:
    def toHex(self, num: int) -> str:
        if not num:
            return '0'

        res = ""
        while num and len(res) != 8:
            x = num & 15
            if x < 10:
                res += str(x)
            else:
                res += chr(x- 10 + ord('a'))
            num >>= 4

        return res[::-1]
