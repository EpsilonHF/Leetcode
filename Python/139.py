"""
Given a non-empty string s and a dictionary wordDict containing 
a list of non-empty words, determine if s can be segmented into 
a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in 
the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as 
"leet code".
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = [False] * len(s)

        for i in range(len(s)):
            for word in wordDict:
            if word == s[i-len(word)+1:i+1] and (d[i-len(word)] or i == len(word) - 1):
                d[i] = True
        
        return d[-1]
