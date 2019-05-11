"""
Given a binary tree, find the length of the longest path where 
each node in the path has the same value. This path may or may 
not pass through the root.

The length of path between two nodes is represented by the number 
of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0

        ret = 0

        def dfs(node):
            if not node:
                return 0

            nonlocal ret
            left = dfs(node.left)
            right = dfs(node.right)
            left = left + 1 if node.left and node.val == node.left.val else 0
            right = right + 1 if node.right and node.val == node.right.val else 0
            ret = max(ret, left + right)

            return max(left, right)

        dfs(root)
