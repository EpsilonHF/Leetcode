"""
Find all possible combinations of k numbers that add up to 
a number n, given that only numbers from 1 to 9 can be used 
and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def helper(k, n, pre, start):
            if k == 1 and 10 > n >= start:
                ans.append(pre+[n])
            for i in range(start, 10):
                if n - i < start:
                    break
                helper(k-1, n-i, pre+[i], i+1)

        helper(k, n, [], 1)

        return ans
