"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) 
to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no 
cell has a fresh orange. If this is impossible, return -1 instead.

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def getset(state):
            ret = set()
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == state:
                        ret.add((i, j))

            return ret

        fresh = getset(1)
        rotten = getset(2)

        time = 0
        while len(fresh) > 0:
            turn = set()
            for i, j in fresh:
                if (i+1, j) in rotten or (i-1, j) in rotten or \
                   (i, j+1) in rotten or (i, j-1) in rotten:
                    turn.add((i, j))

            rotten = rotten | turn
            fresh = fresh - turn
            if len(turn) == 0:
                return -1

            time += 1

        return time
