"""
Given a binary tree, return the inorder traversal of its 
nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def helper(node):
            if not node:
                return
            if node.left: helper(node.left)
            ans.append(node.val)
            if node.right: helper(node.right)

        helper(root)

        return ans
