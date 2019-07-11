"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' 
in the diagram below).

The robot can only move either down or right at any point in time. The 
robot is trying to reach the bottom-right corner of the grid (marked 
'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique 
paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        ans = 0
        path = [[0] * (len(obstacleGrid[0])+1) 
                for i in range(len(obstacleGrid)+1)]
        path[0][1] = 1

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]:
                    path[i+1][j+1] = 0
                else:
                    path[i+1][j+1] = path[i][j+1] + path[i+1][j]

        return path[-1][-1]
