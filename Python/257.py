"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []

        def helper(node, path):
            if not node.left and not node.right:
                res.append(path+str(node.val))
            if node.left:
                helper(node.left, path+str(node.val)+'->')
            if node.right:
                helper(node.right, path+str(node.val)+'->')

        if not root:
            return []

        helper(root, "")

        return res
