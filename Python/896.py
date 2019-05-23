"""
An array is monotonic if it is either monotone increasing or 
monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  
An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

Example 1:

Input: [1,2,2,3]
Output: true
"""

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) < 3:
            return True

        des = ins = True

        for i in range(1, len(A)):
            if not (des or ins):
                return False
            elif des and A[i] > A[i-1]:
                des = False
            elif ins and A[i] < A[i-1]:
                ins = False

        return des or ins
