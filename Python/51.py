"""
The n-queens puzzle is the problem of placing n queens on an n×n 
chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' 
placement, where 'Q' and '.' both indicate a queen and an empty space 
respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle 
as shown above.
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs([-1] * n, 0, [], res)

        return res


    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return

        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                tmp = "." * len(nums)
                self.dfs(nums, index+1, path+[tmp[:i]+'Q'+tmp[i+1:]], res)


    def valid(self, nums, n):
        """
        test whether nth column is valid
        """
        for i in range(n):
            if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]:
                return False

        return True
