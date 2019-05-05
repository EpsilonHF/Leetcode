"""
Given a List of words, return the words that can be typed using 
letters of alphabet on only one row's of American keyboard like 
the image below.

Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
"""

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set('qwertyuiop')
        second = set('asdfghjkl')
        third = set('zxcvbnm')

        res = []
        for word in words:
            ele = set(word.lower())
            if ele & first == ele:
                res.append(word)
            elif ele & second == ele:
                res.append(word)
            elif ele & third == ele:
                res.append(word)

        return res
