"""
You are given a string representing an attendance record for 
a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't 
contain more than one 'A' (absent) or more than two continuous 
'L' (late).

You need to return whether the student could be rewarded according 
to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
"""

class Solution:
    def checkRecord(self, s: str) -> bool:
        A = L = 0
        for ch in s:
            if ch == 'A':
                A += 1
                L = 0
            elif ch == 'L':
                L += 1
            else:
                L = 0
            if A > 1 or L > 2:
                return False

        return True
