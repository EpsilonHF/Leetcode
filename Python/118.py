"""
Given a non-negative integer numRows, generate the first 
numRows of Pascal's triangle.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(numRows-1):
            res.append(list(map(lambda x, y: x+y, [0]+res[-1], res[-1]+[0])))

        return res 
