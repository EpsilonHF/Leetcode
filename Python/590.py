"""
Given an n-ary tree, return the postorder traversal of its 
nodes' values.

For example, given a 3-ary tree:

Return its postorder traversal as: [5,6,3,2,4,1].
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret = []
        if root is None:
            return ret

        def helper(node):
            for child in node.children:
                helper(child)
            ret.append(node.val)

        helper(root)

        return ret
