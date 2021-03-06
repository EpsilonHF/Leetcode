"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the 
following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
"""

import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        array = range(1, n + 1)
        k = (k % math.factorial(n)) - 1
        permutation = []

        for i in range(n - 1, -1, -1):
            idx, k = divmod(k, math.factorial(i))
            permutation.append(array.pop(idx))

        return "".join(map(str, permutation))
