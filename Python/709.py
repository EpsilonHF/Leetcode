"""
Implement function ToLowerCase() that has a string parameter str, 
and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"
"""

class Solution:
    def toLowerCase(self, str: str) -> str:
        ret = ""
        for ch in str:
            if ord('A') <= ord(ch) <= ord('Z'):
                ch = chr(ord(ch) + ord('a') - ord('A'))
            ret += ch

        return ret
