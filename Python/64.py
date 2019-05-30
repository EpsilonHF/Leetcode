"""
Given a m x n grid filled with non-negative numbers, find a path 
from top left to bottom right which minimizes the sum of all 
numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        path = [[0] * n for _ in range(m)]
        path[0][0] = grid[0][0]

        for i in range(1, n):
            path[0][i] = path[0][i-1] + grid[0][i]

        for i in range(1, m):
            path[i][0] = path[i-1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                path[i][j] = min(path[i-1][j], path[i][j-1]) + grid[i][j]

        return path[-1][-1]
