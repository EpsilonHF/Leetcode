"""
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if root is None:
            return ans

        nodes = [(root, 0)]
        pre = -1

        for node, level in nodes:
            if node.left:
                nodes.append((node.left, level + 1))
            if node.right:
                nodes.append((node.right, level + 1))
            if pre == level:
                ans[-1].append(node.val)
            else:
                pre = level
                ans.append([node.val])

        return ans
