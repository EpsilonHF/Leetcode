"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every 
node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        ans = True

        def depth(root):
            nonlocal ans
            if root == None:
                return 0

            left = depth(root.left)
            right = depth(root.right)
            if abs(left - right) > 1:
                ans = False

            return max(left, right) + 1

        depth(root)

        return ans
