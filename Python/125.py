"""
Given a string, determine if it is a palindrome, considering 
only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string 
as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalpha() or i.isdigit()]

        return s == s[::-1]
