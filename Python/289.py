"""
According to the Wikipedia's article: "The Game of Life, also known 
simply as Life, is a cellular automaton devised by the British mathematician 
John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) 
or dead (0). Each cell interacts with its eight neighbors (horizontal, 
vertical, diagonal) using the following four rules (taken from the above 
Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by 
under-population.
Any live cell with two or three live neighbors lives on to the next 
generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, 
as if by reproduction.
Write a function to compute the next state (after one update) of the 
board given its current state. The next state is created by applying 
the above rules simultaneously to every cell in the current state, where 
births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        di = [1, 1, 1, 0, 0, -1, -1, -1]
        dj = [1, 0, -1, 1, -1, 1, 0, -1]

        for i in range(len(board)):
            for j in range(len(board[0])):
                num = 0
                for pos in range(8):
                    ni = i + di[pos]
                    nj = j + dj[pos]
                    if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                        if board[ni][nj] == 1 or board[ni][nj] == -1:
                            num += 1
                if board[i][j] == 1:
                    if num < 2 or num > 3:
                        board[i][j] = -1
                elif board[i][j] == 0 and num == 3:
                    board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
