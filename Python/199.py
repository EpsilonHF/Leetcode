"""
Given a binary tree, imagine yourself standing on the right 
side of it, return the values of the nodes you can see ordered 
from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        nodes = [(root, 0)]

        for node, level in nodes:
            if node.right:
                nodes.append((node.right, level+1))
            if node.left:
                nodes.append((node.left, level+1))

        ans = [root.val]
        for i in range(1, len(nodes)):
            if nodes[i][1] > nodes[i-1][1]:
                ans.append(nodes[i][0].val)

        return ans
