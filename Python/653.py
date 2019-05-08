"""
Given a Binary Search Tree and a target number, return true if 
there exist two elements in the BST such that their sum is equal 
to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        vals = []

        def dfs(node):
            if node is None:
                return
            if node.left:
                dfs(node.left)
            vals.append(node.val)
            if node.right:
                dfs(node.right)

        dfs(root)

        start, end = 0, len(vals) - 1

        while start < end:
            if vals[start] + vals[end] == k:
                return True
            elif vals[start] + vals[end] > k:
                end -= 1
            else:
                start += 1

        return False
