"""
In a binary tree, the root node is at depth 0, and children of 
each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, 
but have different parents.

We are given the root of a binary tree with unique values, and 
the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values 
x and y are cousins.

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        nodes = [(root, 0, None)]
        d = dict()

        for node, level, val in nodes:
            d[node.val] = (level, val)
            if node.left:
                nodes.append((node.left, level + 1, node.val))
            if node.right:
                nodes.append((node.right, level + 1, node.val))

        if x not in d or y not in d:
            return False

        l1, p1 = d[x]
        l2, p2 = d[y]

        return l1 == l2 and p1 != p2
