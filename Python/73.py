"""
Given a m x n matrix, if an element is 0, set its entire row and column 
to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_row = set()
        zero_col = set()

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)

        for row in zero_row:
            matrix[row] = [0] * len(matrix[0])

        for col in zero_col:
            for i in range(len(matrix)):
                matrix[i][col] = 0
