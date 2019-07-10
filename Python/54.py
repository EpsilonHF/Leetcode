"""
Given a matrix of m x n elements (m rows, n columns), return all elements 
of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        ans = []
        
        while matrix:
            ans += matrix[0]
            matrix = zip(*matrix[1:])
            matrix = matrix[::-1]
            
        return ans
