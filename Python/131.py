"""
Given a string s, partition s such that every substring of the partition 
is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.palind(s, [], res)

        return res


    def palind(self, s, path, res):

        if len(s) == 0:
            res.append(path)
            return

        for i in range(len(s)):
            new = s[:i+1]
            if new == new[::-1]:
                self.palind(s[i+1:], path + [new], res)
