"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 
9 and 15 respectively. Return 24.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def helper(node, is_left):
            if not node:
                return 0
            if is_left and not node.left and not node.right:
                return node.val
            else:
                return helper(node.left, True) + helper(node.right, False)

        return helper(root, False)
