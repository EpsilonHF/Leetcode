"""
Given a positive integer n, find the least number of perfect square 
numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
"""

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [i for i in range(n+1)]
        for i in range(2, n+1):
            j = 1
            while j * j <= i:
                ans[i] = min(ans[i], ans[i-j*j] + 1)
                j += 1

        return ans[n]
