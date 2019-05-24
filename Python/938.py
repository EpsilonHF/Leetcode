"""
Given the root node of a binary search tree, return the sum of 
values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        ret = 0

        def dfs(node):
            nonlocal ret
            if node is None:
                return
            if node.val < L and node.right:
                dfs(node.right)
            elif node.val > R and node.left:
                dfs(node.left)
            elif L <= node.val <= R:
                ret += node.val
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        return ret
