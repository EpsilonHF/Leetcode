"""
The string "PAYPALISHIRING" is written in a zigzag pattern 
on a given number of rows like this: (you may want to display 
this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        strings = [""] * numRows
        i = 0
        d = 1

        for ch in s:
            strings[i] += ch
            if i == 0: d = 1
            elif i == numRows - 1: d = -1
            i += d

        return "".join(strings)
