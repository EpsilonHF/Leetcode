"""
A boomerang is a set of 3 points that are all distinct and not 
in a straight line.

Given a list of three points in the plane, return whether these 
points are a boomerang.

Example 1:

Input: [[1,1],[2,3],[3,2]]
Output: true
"""

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:

        a1 = points[1][0] - points[0][0]
        b1 = points[1][1] - points[0][1]
        a2 = points[2][0] - points[0][0]
        b2 = points[2][1] - points[0][1]

        return a1 * b2 - a2 * b1 != 0
