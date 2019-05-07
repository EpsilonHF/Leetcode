"""
Given two non-empty binary trees s and t, check whether tree 
t has exactly the same structure and node values with a subtree 
of s. A subtree of s is a tree consists of a node in s and all 
of this node's descendants. The tree s could also be considered 
as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values 
with a subtree of s.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def same(s, t):
            if s and t:
                if s.val != t.val:
                    return False

                return same(s.left, t.left) and same(s.right, t.right)

            if not s and not t:
                return True

            return False

        if s is None:
            return False

        return same(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
