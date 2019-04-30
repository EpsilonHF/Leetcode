"""
You have a total of n coins that you want to form in a staircase 
shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that 
can be formed.

n is a non-negative integer and fits within the range of a 
32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        num = int((n * 2) ** 0.5)

        if n < num * (num + 1) // 2:
            return num - 1
        else:
            return num