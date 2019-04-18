"""
Given a binary tree containing digits from 0-9 only, each 
root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents 
the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = 0

        def helper(node, num = 0):
            nonlocal ans
            if node is None:
                return
            if node.left is None and node.right is None:
                ans += num * 10 + node.val
            else:
                helper(node.left, num*10+node.val)
                helper(node.right, num*10+node.val)

        helper(root)

        return ans
