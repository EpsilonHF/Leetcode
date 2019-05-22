"""
Consider all the leaves of a binary tree. From left to right 
order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence 
is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value 
sequence is the same.

Return true if and only if the two given trees with head nodes 
root1 and root2 are leaf-similar.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def dfs(node, leaf):
            if node.left:
                dfs(node.left, leaf)
            if not node.left and not node.right:
                leaf.append(node.val)
            if node.right:
                dfs(node.right, leaf)

        l1 = []
        l2 = []

        dfs(root1, l1)
        dfs(root2, l2)

        return l1 == l2
