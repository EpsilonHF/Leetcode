"""
Given a string, find the first non-repeating character in it 
and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(x) for x in letter if s.count(x) == 1]

        return min(index) if len(index) else -1
