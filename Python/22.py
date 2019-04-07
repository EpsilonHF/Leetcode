"""
Given n pairs of parentheses, write a function to generate 
all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def form(s, left, right):
            if len(s) == 2*n:
                ans.append(s)
                return None
            if left < n:
                form(s+'(', left+1, right)
            if right < left:
                form(s+')', left, right+1)

        form('', 0, 0)
        return ans
