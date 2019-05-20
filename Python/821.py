"""
Given a string S and a character C, return an array of integers 
representing the shortest distance from the character C in the 
string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
"""

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        ret = [0] * len(S)

        for index, ch in enumerate(S):
            if ch == C:
                ret[index] = 0
            else:
                ret[index] = ret[index-1]+1 if index else len(S)

        for i in range(len(S)-2, -1, -1):
            ret[i] = min(ret[i+1] + 1, ret[i])

        return ret
