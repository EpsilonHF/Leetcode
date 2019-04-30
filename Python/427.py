"""
We want to use quad trees to store an N x N boolean grid. 
Each cell in the grid can only be true or false. The root 
node represents the whole grid. For each node, it will be 
subdivided into four children nodes until the values in the 
region it represents are all the same.

Each node has another two boolean attributes : isLeaf and val. 
isLeaf is true if and only if the node is a leaf node. The val 
attribute for a leaf node contains the value of the region it 
represents.

Your task is to use a quad tree to represent a given grid. The 
following example may help you understand the problem better:

Given the 8 x 8 grid below, we want to construct the corresponding 
quad tree:
"""

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        same = True
        for row in grid:
            for num in row:
                if num != grid[0][0]:
                    same = False
                    break
        
        if same:
            node = Node(grid[0][0], True, None, None, None, None)
        
        else:
            mid = len(grid) // 2
            topLeft = self.construct([row[:mid] for row in grid[:mid]])
            topRight = self.construct([row[mid:] for row in grid[:mid]])
            bottomLeft = self.construct([row[:mid] for row in grid[mid:]])
            bottomRight = self.construct([row[mid:] for row in grid[mid:]])
            node = Node(None, False, topLeft, topRight, bottomLeft, bottomRight)

        return node

