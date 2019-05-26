"""
Given an array A of strings made only from lowercase letters, 
return a list of all characters that show up in all strings within 
the list (including duplicates).  For example, if a character 
occurs 3 times in all strings but not 4 times, you need to include 
that character three times in the final answer.

You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
"""

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        lst_d = []
        for word in A:
            d = {word: 0 for word in "abcdefghijklmnopqrstuvwxyz"}
            for e in word:
                d[e] += 1
            lst_d.append(d)
        
        ret = []
        
        for key in lst_d[0]:
            num = min(d[key] for d in lst_d)
            ret += [key] * num
            
        return ret
