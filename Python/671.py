"""
Given a non-empty special binary tree consisting of nodes with
the non-negative value, where each node in this tree has exactly 
two or zero sub-node. If the node has two sub-nodes, then this 
node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum 
value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root or not root.left :
            return -1

        if root.left.val > root.val and root.right.val > root.val:
            return min(root.left.val, root.right.val)

        if root.left.val > root.val:
            ret = self.findSecondMinimumValue(root.right)
            if ret == -1:
                return root.left.val
            return min(ret, root.left.val)

        if root.right.val > root.val:
            ret = self.findSecondMinimumValue(root.left)
            if ret == -1:
                return root.right.val
            return min(ret, root.right.val)

        ret1 = self.findSecondMinimumValue(root.right)
        ret2 = self.findSecondMinimumValue(root.left)

        if ret1 > root.val and ret2 > root.val:
            return min(ret1, ret2)

        elif max(ret1, ret2) > root.val:
            return max(ret1, ret2)

        else:
            return -1
