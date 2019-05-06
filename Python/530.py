"""
Given a binary search tree with non-negative values, find the 
minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference 
between 2 and 1 (or between 2 and 3).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        vals = []

        def dfs(node):
            if node.left:
                dfs(node.left)
            vals.append(node.val)
            if node.right:
                dfs(node.right)

        dfs(root)
        res = float("inf")
        for i in range(1, len(vals)):
            res = min(res, abs(vals[i] - vals[i-1]))

        return res
