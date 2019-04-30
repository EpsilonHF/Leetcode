"""
Given an n-ary tree, return the level order traversal of its 
nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:

We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        nodes = [(root, 0)]
        res = []
        pre = -1
        for node, level in nodes:
            if node.children:
                for child in node.children:
                    nodes.append((child, level + 1))
            if level == pre:
                res[-1].append(node.val)
            else:
                res.append([node.val])
                pre = level

        return res
