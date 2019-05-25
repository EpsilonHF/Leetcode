"""
In an alien language, surprisingly they also use english lowercase 
letters, but possibly in a different order. The order of the 
alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the 
order of the alphabet, return true if and only if the given words 
are sorted lexicographicaly in this alien language.

Example 1:

Input: 
words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: 
As 'h' comes before 'l' in this language, then the sequence is sorted.
"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {order[num]: num for num in range(len(order))}

        for i in range(1, len(words)):
            for index in range(len(words[i-1])):
                if index >= len(words[i]):
                    return False

                if d[words[i-1][index]] > d[words[i][index]]:
                    return False

                if d[words[i-1][index]] < d[words[i][index]]:
                    break

        return True
