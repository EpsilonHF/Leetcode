"""
Given a string s and a non-empty string p, find all the start 
indices of p's anagrams in s.

Strings consists of lowercase English letters only and the 
length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        def hashtable(string):
            table = [0] * 26
            for ch in string:
                table[ord(ch) - ord('a')] += 1
            return table

        words = set(p)
        phash = hashtable(p)
        shash = hashtable(s[:len(p)])
        res = []
        i = len(p)

        while i < len(s):
            if phash == shash:
                res.append(i - len(p))
            if s[i] not in words:
                i += len(p) + 1
                shash = hashtable(s[i-len(p):i])
            else:
                shash[ord(s[i]) - ord('a')] += 1
                shash[ord(s[i-len(p)]) - ord('a')] -= 1
                i += 1

        if phash == shash:
            res.append(i - len(p))

        return res
