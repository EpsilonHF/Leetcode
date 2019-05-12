"""
We have two special characters. The first character can be 
represented by one bit 0. The second character can be represented 
by two bits (10 or 11).

Now given a string represented by several bits. Return whether 
the last character must be a one-bit character or not. The given 
string will always end with a zero.

Example 1:
Input:
bits = [1, 0, 0]
Output: True
Explanation:
The only way to decode it is two-bit character and one-bit character. 
So the last character is one-bit character.
"""

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        pos = 0
        onebit = False

        while pos < len(bits):
            if bits[pos]:
                pos += 2
                onebit = False
            else:
                pos += 1
                onebit = True

        return onebit
