"""
In a string S of lowercase letters, these letters form consecutive 
groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", 
"bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like 
the starting and ending positions of every large group.

The final answer should be in lexicographic order.

Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting 3 and 
ending positions 6.
"""

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        count = 1
        ret = []
        start = 0
        for i in range(1, len(S)):
            if S[i] == S[i-1]:
                count += 1
            else:
                if count >= 3:
                    ret.append([start, i-1])
                start = i
                count = 1

        if count >= 3:
            ret.append([start, len(S)-1])

        return ret
