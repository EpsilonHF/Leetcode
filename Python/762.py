"""
Given two integers L and R, find the count of numbers in the 
range [L, R] (inclusive) having a prime number of set bits in 
their binary representation.

(Recall that the number of set bits an integer has is the number 
of 1s present when written in binary. For example, 21 written in 
binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

Example 1:

Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
"""

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        prime = [2, 3, 5, 7, 11, 13, 17, 19]
        ret = 0
        for i in range(L, R+1):
            count = 0
            num = i
            while num:
                count += num & 1
                num >>= 1
            ret += 1 if count in prime else 0

        return ret
