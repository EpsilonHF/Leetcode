"""
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed 
on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

Example 1:

Input: [[2]]
Output: 10
"""

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ret = 0
        R, C = len(grid), len(grid[0])

        for row in range(R):
            for col in range(C):
                if grid[row][col]:
                    ret += 2
                    for i, j in [(row-1, col), (row+1, col), (row, col-1),
                                 (row, col + 1)]:

                        if 0 <= i < R and 0<= j < C:
                            val = grid[i][j]
                        else:
                            val = 0

                        ret += max(0, grid[row][col] - val)

        return ret
