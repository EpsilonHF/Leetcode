"""
In a town, there are N people labelled from 1 to N. There is 
a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing 
that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the 
label of the town judge. Otherwise, return -1.

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
"""

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1

        cand = set(range(1, N+1)) - set(i[0] for i in trust)
        if len(cand) < 1:
            return -1

        d = dict()
        for _, p in trust:
            if p in cand:
                d[p] = d.get(p, 0) + 1

        for key in d:
            if d[key] == N - 1:
                return key

        return -1
