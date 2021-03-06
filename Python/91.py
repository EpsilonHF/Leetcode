"""
A message containing letters from A-Z is being encoded to numbers using 
the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total 
number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
"""

class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == "0":
            return 0
        dp1 = dp2 = 1

        for i in range(1, len(s)):
            if s[i] == "0" and (s[i-1] == "0" or s[i-1] >= "3"):
                return 0

            if s[i] == "0":
                dp1, dp2 = dp2, dp1
            elif "10" <= s[i-1:i+1] <= "26":
                dp1, dp2 = dp2, dp2 + dp1
            else:
                dp1, dp2 = dp2, dp2

        return dp2
