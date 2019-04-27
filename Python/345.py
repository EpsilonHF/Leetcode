"""
Write a function that takes a string as input and reverse only 
the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        words = list(s)
        vowel = set(list("aeiouAEIOU"))
        start, end = 0, len(s) - 1
        while start < end:
            if words[start] not in vowel:
                start += 1
            elif words[end] not in vowel:
                end -= 1
            else:
                words[start], words[end] = words[end], words[start]
                start += 1
                end -= 1

        return ''.join(words)
