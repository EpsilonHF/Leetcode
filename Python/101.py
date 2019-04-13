"""
Given a binary tree, check whether it is a mirror of itself 
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def mirror(s, t):
            if not s and not t:
                return True
            elif not s or not t:
                return False
            else:
                return s.val == t.val and mirror(s.left, t.right) and mirror(s.right, t.left)

        return mirror(root, root)
