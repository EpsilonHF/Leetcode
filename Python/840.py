"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers 
from 1 to 9 such that each row, column, and both diagonals all 
have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids 
are there? (Each subgrid is contiguous).

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
"""

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0

        for row in range(1, len(grid)-1):
            for col in range(1, len(grid[0])-1):
                if grid[row][col] != 5:
                    continue

                s = "".join(str(grid[row - 1 + x // 3][col -1 + x % 3])
                            for x in [0, 1, 2, 5, 8, 7, 6, 3])

                if s in "43816729" * 2 or s in "43816729"[::-1] * 2:
                    count += 1

        return count
