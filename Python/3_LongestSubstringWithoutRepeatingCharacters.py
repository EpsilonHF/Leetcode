"""
Given a string, find the length of the longest substring 
without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num = 0
        pre = 0
        letters = dict()

        for i in range(len(s)):
            if s[i] not in s[j:i]:
                letters[s[i]] = i
                num = max(num, i-pre+1)
            else:
                pre = letters[s[i]]+1
                letters[s[i]] = i
        return num
