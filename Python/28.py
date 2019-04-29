"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        return haystack.find(needle)
