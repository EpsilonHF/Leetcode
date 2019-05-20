"""
Given a string S, return the "reversed" string where all characters 
that are not a letter stay in the same place, and all letters 
reverse their positions.

Example 1:

Input: "ab-cd"
Output: "dc-ba"
"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        i, j = 0, len(S) - 1
        S = list(S)

        while i < j:
            while i < j and not S[i].isalpha():
                i += 1
            while i < j and not S[j].isalpha():
                j -= 1

            S[i], S[j] = S[j], S[i]
            i, j = i + 1, j - 1

        return "".join(S)
