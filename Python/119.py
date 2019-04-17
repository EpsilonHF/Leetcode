"""
Given a non-negative index k where k ≤ 33, return the kth 
index row of the Pascal's triangle.

Note that the row index starts from 0.

Example:

Input: 3
Output: [1,3,3,1]
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for _ in range(rowIndex):
            ans = list(map(lambda x, y: x + y, [0]+ans, ans+[0]))

        return ans
