"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        d = dict()

        for word in strs:
            ch = [0] * 26
            for e in word:
                ch[ord(e) - 97] += 1
            key = tuple(ch)

            if key not in d:
                ret.append([word])
                d[key] = len(ret)
            else:
                ret[d[key]-1].append(word)

        return ret
