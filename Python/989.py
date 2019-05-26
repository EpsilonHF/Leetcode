"""
For a non-negative integer X, the array-form of X is an array 
of its digits in left to right order. For example, if X = 1231, 
then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the 
array-form of the integer X+K.

Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
"""

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        num = 0
        for i in range(len(A)):
            num = num * 10 + A[i]

        num += K
        return list(map(int, str(num)))
