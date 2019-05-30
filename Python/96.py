"""
Given n, how many structurally unique BST's (binary search trees) 
that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        vals = [0, 1, 2] + [0] * (n-2)
        
        for i in range(3, n+1):
            num1 = 2 * vals[i-1]
            num2 = 0
            for j in range(1, i-1):
                num2 += vals[j] * vals[i-j-1]
            vals[i] = num1 + num2
        
        return vals[n]
