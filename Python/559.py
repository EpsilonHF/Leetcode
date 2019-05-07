"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest 
path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        if not root.children:
            return 1

        return max(self.maxDepth(node) for node in root.children) + 1
