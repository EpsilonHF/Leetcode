"""
On an infinite plane, a robot initially stands at (0, 0) and 
faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats 
them forever.

Return true if and only if there exists a circle in the plane 
such that the robot never leaves the circle.

Example 1:

Input: "GGLLGG"
Output: true
Explanation:
The robot moves from (0,0) to (0,2), turns 180 degrees, and then 
returns to (0,0).
When repeating these instructions, the robot remains in the circle 
of radius 2 centered at the origin.
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        x, y = 0, 0

        for move in 4 * instructions:
            if move == 'L':
                i = (i - 1) % 4
            elif move == 'R':
                i = (i + 1) % 4
            else:
                x += direct[i][0]
                y += direct[i][1]

        return not x and not y
