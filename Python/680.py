"""
Given a non-empty string s, you may delete at most one character. 
Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start < end and s[start] == s[end]:
            start += 1
            end -= 1

        if start >= end:
            return True

        string1 = s[start:end]
        string2 = s[start+1:end+1]

        return string1 == string1[::-1] or string2 == string2[::-1]
