"""
Given an array A of 0s and 1s, consider N_i: the i-th subarray 
from A[0] to A[i] interpreted as a binary number (from most-significant-bit 
to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and 
only if N_i is divisible by 5.

Example 1:

Input: [0,1,1]
Output: [true,false,false]
Explanation:
The input numbers in binary are 0, 01, 011; which are 0, 1, 
and 3 in base-10. Only the first number is divisible by 5, so 
answer[0] is true.
"""

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        num = [0] * len(A)
        num[0] = A[0]

        for i in range(1, len(A)):
            num[i] = num[i-1] * 2 + A[i]

        return [i % 5 == 0 for i in num]
