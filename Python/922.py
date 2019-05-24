"""
Given an array A of non-negative integers, half of the integers 
in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and 
whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: 
[4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
"""

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        B = [0] * len(A)
        odd, even = 1, 0
        
        for num in A:
            if num % 2:
                B[odd] = num
                odd += 2
            else:
                B[even] = num
                even += 2
        
        return B


