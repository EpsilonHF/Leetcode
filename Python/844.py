"""
Given two strings S and T, return if they are equal when both 
are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s1 = []
        s2 = []

        for ch in S:
            if ch != "#":
                s1.append(ch)
            elif len(s1):
                s1.pop()

        for ch in T:
            if ch != "#":
                s2.append(ch)
            elif len(s2):
                s2.pop()

        return ''.join(s1) == ''.join(s2)
