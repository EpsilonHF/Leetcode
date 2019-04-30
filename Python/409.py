"""
Given a string which consists of lowercase or uppercase letters, 
find the length of the longest palindromes that can be built 
with those letters.

This is case sensitive, for example "Aa" is not considered a 
palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose 
length is 7.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = dict()
        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        length = flag = 0
        for ch in d:
            if d[ch] % 2:
                flag = 1
                length += d[ch] - 1
            else:
                length += d[ch]

        return length + flag
