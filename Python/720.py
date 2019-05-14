"""
Given a list of strings words representing an English Dictionary, 
find the longest word in words that can be built one character at 
a time by other words in words. If there is more than one possible 
answer, return the longest word with the smallest lexicographical 
order.

If there is no answer, return the empty string.
Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", 
"wor", and "worl".
"""

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words_map = set()
        for word in words:
            words_map.add(word)

        ret = ""
        for word in words:
            flag = True
            for i in range(1, len(word)):
                if word[:i] not in words_map:
                    flag = False
                    break
            if flag:
                if len(word) > len(ret):
                    ret = word
                elif len(word) == len(ret) and word < ret:
                    ret = word

        return ret
