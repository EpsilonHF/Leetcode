"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the 
node's key.
The right subtree of a node contains only nodes with keys greater than 
the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, node, low, high):
        if node is None:
            return True
        if node.val >= high or node.val <= low:
            return False
        if node.left and (node.val <= node.left.val or node.left.val <= low) :
            return False
        if node.right and \
           (node.val >= node.right.val or node.right.val >= high):
            return False
        return self.valid(node.left, low, node.val) and \
               self.valid(node.right, node.val, high)
