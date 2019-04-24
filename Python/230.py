"""
Given a binary search tree, write a function kthSmallest to 
find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans = []
        def helper(node):
            if node is None:
                return None
            if node.left:
                helper(node.left)
            ans.append(node.val)
            if node.right:
                helper(node.right)

        helper(root)

        return ans[k-1]
