"""
Given a binary tree, return the bottom-up level order traversal 
of its nodes' values. (ie, from left to right, level by level 
from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        res = []
        pre = 0
        nodes = [(root, 1)]
        for node, level in nodes:
            if level == pre:
                res[-1].append(node.val)
            else:
                res.append([node.val])
                pre = level

            if node.left:
                nodes.append((node.left, level + 1))
            if node.right:
                nodes.append((node.right, level + 1))

        return res[::-1]
