"""
A robot is located at the top-left corner of a m x n grid 
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point 
in time. The robot is trying to reach the bottom-right corner 
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        step = m + n - 2
        num = min(m - 1, n - 1)
        ans = 1
        for i in range(num):
            ans = ans * (step - i) // (i + 1)

        return ans
