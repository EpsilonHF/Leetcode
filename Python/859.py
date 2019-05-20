"""
Given two strings A and B of lowercase letters, return true 
if and only if we can swap two letters in A so that the result 
equals B.

 Example 1:

 Input: A = "ab", B = "ba"
 Output: true
"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
                                        
        if A == B and len(A) > len(set(A)):
            return True
                                                            
        re1 = ""
        re2 = ""
        for i in range(len(A)):
            if A[i] != B[i]:
                re1 += A[i]
                re2 += B[i] 
        
        if len(re1) == len(re2) == 2 and re1 == re2[::-1]:         
            return True
        
        return False
