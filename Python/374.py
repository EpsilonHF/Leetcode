"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number 
I picked.

Every time you guess wrong, I'll tell you whether the number 
is higher or lower.

You call a pre-defined API guess(int num) which returns 3 
possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n

        while low < high:
            mid = (low + high) // 2
            n = guess(mid)
            if n == 0:
                return mid
            elif n > 0:
                low = mid + 1
            else:
                high = mid - 1

        return low
