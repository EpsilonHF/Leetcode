"""
You have N gardens, labelled 1 to N. In each garden, you want 
to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional 
path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into 
or leaving it.

Your task is to choose a flower type for each garden such that, 
for any two gardens connected by a path, they have different 
types of flowers.

Return any such a choice as an array answer, where answer[i] is 
the type of flower planted in the (i+1)-th garden. The flower 
types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

Example 1:

Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
"""

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        G = [[] for i in range(N)]
        ret = [0] * N

        for x, y in paths:
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)

        for i in range(N):
            ret[i] = ({1, 2, 3, 4} - {ret[j] for j in G[i]}).pop()

        return ret
