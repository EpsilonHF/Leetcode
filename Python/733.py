"""
An image is represented by a 2-D array of integers, each integer 
representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel 
(row and column) of the flood fill, and a pixel value newColor, 
"flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any 
pixels connected 4-directionally to the starting pixel of the same 
color as the starting pixel, plus any pixels connected 4-directionally 
to those pixels (also with the same color as the starting pixel), 
and so on. Replace the color of all of the aforementioned pixels 
with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), 
all pixels connected by a path of the same color as the starting 
pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally 
connected to the starting pixel.
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldcolor = image[sr][sc]
        if oldcolor == newColor:
            return image

        pos = [(sr, sc)]
        row_len = len(image)
        col_len = len(image[0])
        trace = [[1]*col_len for _ in range(row_len)]

        for row, col in pos:
            image[row][col] = newColor
            trace[row][col] = 0

            if row + 1 < row_len and trace[row+1][col] and image[row+1][col] == oldcolor:
                pos.append((row+1, col))

            if row - 1 >= 0 and trace[row-1][col] and image[row-1][col] == oldcolor:
                pos.append((row-1, col))

            if col + 1 < col_len and trace[row][col+1] and image[row][col+1] == oldcolor:
                pos.append((row, col+1))

            if col - 1 >= 0 and trace[row][col-1] and image[row][col-1] == oldcolor:
                pos.append((row, col-1))

        return image
