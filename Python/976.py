"""
Given an array A of positive lengths, return the largest perimeter 
of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.

Example 1:

Input: [2,1,2]
Output: 5
"""

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse = True)
        i = 0

        while i < len(A) - 2:
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
            else:
                i += 1

        return 0
