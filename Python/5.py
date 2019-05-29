"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ""
        MAX = 0

        for center in range(len(s)):
            i = 0

            while center - i >= 0 and center + i < len(s):
                if s[center + i] != s[center - i]:
                    break
                i += 1

            if 2 * i - 1 > MAX:
                MAX = 2 * i - 1
                ret = s[center-i+1: center+i]

        for center in range(len(s) - 1):
            i = 0

            while center - i >= 0 and center + i + 1 < len(s):
                if s[center + i + 1] != s[center - i]:
                    break
                i += 1

            if 2 * i > MAX:
                MAX = 2 * i
                ret = s[center - i + 1: center + i + 1]

        return ret
