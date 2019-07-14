"""
Given a 2d grid map of '1's (land) and '0's (water), count the number 
of islands. An island is surrounded by water and is formed by connecting 
adjacent lands horizontally or vertically. You may assume all four edges 
of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        seen = [[0] * len(grid[0]) for i in range(len(grid))]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        number = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if seen[i][j] == 1:
                    continue
                if grid[i][j] == "0":
                    continue
                number += 1
                stack = [(i, j)]

                while stack:

                    r, c = stack.pop()
                    seen[r][c] = 1

                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]

                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and \
                           seen[nr][nc] == 0 and grid[nr][nc] == "1":
                            stack.append((nr, nc))

        return number
