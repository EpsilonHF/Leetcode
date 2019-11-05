"""
Given an integer n, generate all structurally unique BST's (binary 
search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.gen(1, n)

    def gen(self, l, r):
        res = []

        if l > r:
            res.append(None)
        for i in range(l, r+1):
            left = self.gen(l, i-1)
            right = self.gen(i+1, r)

            for leftnode in left:
                for rightnode in right:
                    root = TreeNode(i)
                    root.left = leftnode
                    root.right = rightnode
                    res.append(root)

        return res
