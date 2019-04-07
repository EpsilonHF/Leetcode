"""
Given a string containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        chars = {
            '[': 0, ']': 0,
            '{': 1, '}': 1,
            '(': 2, ')': 2,
        }
        stack = []
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if chars[p] != chars[ch]:
                    return False

        return len(stack) == 0
