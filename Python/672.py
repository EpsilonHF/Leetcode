"""
There is a room with n lights which are turned on initially and 
4 buttons on the wall. After performing exactly m unknown operations 
towards buttons, you need to return how many different kinds of 
status of the n lights could be.

Suppose n lights are labeled as number [1, 2, 3 ..., n], function 
of these 4 buttons are given below:

Flip all the lights.
Flip lights with even numbers.
Flip lights with odd numbers.
Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...

Example 1:

Input: n = 1, m = 1.
Output: 2
Explanation: Status can be: [on], [off]
"""

class Solution:
    def flipLights(self, n: int, m: int) -> int:
        if m == 0:
            return 1

        elif n <= 0 or m < 0:
            return 0

        elif n == 1:
            return 2

        elif n == 2:
            if m == 1:
                return 3
            else:
                return 4

        else:
            if m == 1:
                return 4
            elif m == 2:
                return 7
            else:
                return 8
