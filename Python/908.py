"""
Given an array A of integers, for each integer A[i] we may choose 
any x with -K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value 
of B and the minimum value of B.

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
"""

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:

        return max(0, max(A) - min(A) - 2 * K)
