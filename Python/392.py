"""
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters 
in both s and t. t is potentially a very long (length ~= 500,000) 
string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from 
the original string by deleting some (can be none) of the 
characters without disturbing the relative positions of the 
remaining characters. (ie, "ace" is a subsequence of "abcde" 
while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        i = 0
        for ch in t:
            if s[i] == ch:
                i += 1
            if i == len(s):
                return True

        return False
