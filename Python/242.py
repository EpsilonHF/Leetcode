"""
Given two strings s and t , write a function to determine if 
t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = dict()
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        for ch in t:
            if ch not in d:
                return False
            if d[ch] < 1:
                return False
            d[ch] -= 1

        return True
