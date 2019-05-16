"""
Given a string S, we can transform every letter individually 
to be lowercase or uppercase to create another string. Return 
a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
"""

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if len(S) == 0:
            return [""]
        
        if S[0].isalpha():
            return [start + ch for ch in self.letterCasePermutation(S[1:])
                               for start in [S[0].upper(), S[0].lower()]]
        
        else:
            return [S[0] + ch for ch in self.letterCasePermutation(S[1:])]
