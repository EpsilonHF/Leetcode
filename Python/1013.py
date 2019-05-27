"""
Given an array A of integers, return true if and only if we can 
partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes 
i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... 
+ A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

Example 1:

Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
"""

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3:
            return False

        targets = [s // 3 * 2, s // 3]
        acc = 0

        for a in A:
            acc += a
            if acc == targets[-1]:
                targets.pop()
            if not targets:
                return True

        return False
