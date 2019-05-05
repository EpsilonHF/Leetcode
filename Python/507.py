"""
We define the Perfect Number is a positive integer that is 
equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true 
when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        perfect = [6, 28, 496, 8128, 33550336]
        if num in perfect:
            return True

        return False
