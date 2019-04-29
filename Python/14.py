"""
Write a function to find the longest common prefix string 
amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        if len(strs) == 0:
            return s

        for i in range(len(strs[0])):
            s = strs[0][:i+1]

            for str in strs:
                if not str.startswith(s):
                    return s[:-1]

        return s
