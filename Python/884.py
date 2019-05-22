"""
We are given two sentences A and B. (A sentence is a string of 
space separated words. Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the 
sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
"""

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        ret = []
        d1 = dict()
        d2 = dict()

        for word in A.split():
            d1[word] = d1.get(word, 0) + 1

        for word in B.split():
            d2[word] = d2.get(word, 0) + 1

        for key in d1:
            if d1[key] == 1 and key not in d2:
                ret.append(key)

        for key in d2:
            if d2[key] == 1 and key not in d1:
                ret.append(key)

        return ret
