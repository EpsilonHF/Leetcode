"""
Given a non-empty binary tree, return the average value of the 
nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, 
and on level 2 is 11. Hence return [3, 14.5, 11].
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return []

        total = dict()
        num = dict()
        nodes = [(root, 0)]
        for node, level in nodes:
            total[level] = total.get(level, 0) + node.val
            num[level] = num.get(level, 0) + 1
            if node.left:
                nodes.append((node.left, level + 1))
            if node.right:
                nodes.append((node.right, level + 1))

        return [total[level]/num[level] for level in total]
