"""
Given a string array words, find the maximum value of 
length(word[i]) * length(word[j]) where the two words do not 
share common letters. You may assume that each word will 
contain only lower case letters. If no such two words exist, 
return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
"""

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if len(words) < 2:
            return 0

        ans = 0
        value = []
        for word in words:
            val = 0
            for ch in word:
                val |= 1 << (ord(ch) - ord('a'))
            value.append(val)

        for i in range(len(value)):
            for j in range(i+1, len(value)):
                if value[i] & value[j] == 0:
                    ans = max(ans, len(words[i])*len(words[j]))

        return ans
