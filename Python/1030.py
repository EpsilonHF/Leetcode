"""
We are given a matrix with R rows and C columns has cells with 
integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.

Additionally, we are given a cell in that matrix with coordinates 
(r0, c0).

Return the coordinates of all cells in the matrix, sorted by their 
distance from (r0, c0) from smallest distance to largest distance.  
Here, the distance between two cells (r1, c1) and (r2, c2) is the 
Manhattan distance, |r1 - r2| + |c1 - c2|. (You may return the answer 
in any order that satisfies this condition.)

Example 1:

Input: R = 1, C = 2, r0 = 0, c0 = 0
Output: [[0,0],[0,1]]
Explanation: The distances from (r0, c0) to other cells are: [0,1]
"""

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ret = [[] for _ in range(R + C)]

        for row in range(R):
            for col in range(C):
                ret[abs(row - r0) + abs(col - c0)].append([row, col])

        return sum(ret, [])
