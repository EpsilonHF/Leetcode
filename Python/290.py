"""
Given a pattern and a string str, find if str follows the 
same pattern.

Here follow means a full match, such that there is a bijection 
between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
"""

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d1 = dict()
        d2 = dict()
        words = str.split()

        if len(words) != len(pattern):
            return False

        for i in range(len(words)):
            if words[i] not in d1 and pattern[i] not in d2:
                d1[words[i]] = pattern[i]
                d2[pattern[i]] = words[i]
            if words[i] in d1 and pattern[i] in d2:
                if d1[words[i]] != pattern[i] or d2[pattern[i]] != words[i]:
                    return False
            else:
                return False

        return True
