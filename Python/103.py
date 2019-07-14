"""
Given a binary tree, return the zigzag level order traversal of its 
nodes' values. (ie, from left to right, then right to left for the 
next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if root is None:
            return ans

        pre = -1
        nodes = [(root, 0)]

        for node, level in nodes:
            if node.left:
                nodes.append((node.left, level+1))
            if node.right:
                nodes.append((node.right, level+1))
            if level == pre:
                ans[-1].append(node.val)
            else:
                pre = level
                ans.append([node.val])

        for i in range(len(ans)):
            if i % 2:
                ans[i] = ans[i][::-1]

        return ans
