"""
You are given an array A of strings.

Two strings S and T are special-equivalent if after any number 
of moves, S == T.

A move consists of choosing two indices i and j with i % 2 == j % 2, 
and swapping S[i] with S[j].

Now, a group of special-equivalent strings from A is a non-empty 
subset S of A such that any string not in S is not special-equivalent 
with any string in S.

Return the number of groups of special-equivalent strings from A.

Example 1:

Input: ["a","b","c","a","c","c"]
Output: 3
Explanation: 3 groups ["a","a"], ["b"], ["c","c","c"]
"""

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:

        def count(A):
            ans = [0] * 52
            for i, ch in enumerate(A):
                ans[ord(ch) - ord('a') + 26 * (i % 2)] += 1

            return tuple(ans)

        return len(set(count(word) for word in A))
