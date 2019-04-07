"""
Given a string containing digits from 2-9 inclusive, return 
all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone 
buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        letter = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        num = int(digits)

        def helper(num):
            if num < 10:
                return [ch for ch in letter[num-2]]
            else:
                return [res+ch for ch in letter[num%10-2]
                               for res in helper(num//10)]

        return helper(num)
