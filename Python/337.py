"""
The thief has found himself a new place for his thievery again. 
There is only one entrance to this area, called the "root." 
Besides the root, each house has one and only one parent house. 
After a tour, the smart thief realized that "all houses in this 
place forms a binary tree". It will automatically contact the 
police if two directly-linked houses were broken into on the 
same night.

Determine the maximum amount of money the thief can rob tonight 
without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: 
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        d = dict()

        def helper(node):
            if node is None:
                return 0
            if node in d:
                return d[node]
            val = 0

            if node.left:
                val += helper(node.left.left) + helper(node.left.right)
            if node.right:
                val += helper(node.right.left) + helper(node.right.right)
            val = max(val+node.val, helper(node.left)+helper(node.right))
            d[node] = val

            return val

        return helper(root)
