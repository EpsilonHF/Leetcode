"""
A robot on an infinite grid starts at point (0, 0) and faces north.  
The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles.

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the 
previous grid square instead (but still continues following the 
rest of the route.)

Return the square of the maximum Euclidean distance that the robot 
will be from the origin.

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
"""

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        pos = [0, 0]
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        obstacleSet = set(map(tuple, obstacles))
        i = dist = 0

        for command in commands:
            if command == -1:
                i = (i + 1) % 4
            elif command == -2:
                i = (i - 1) % 4
            else:
                direct = d[i]
                while command:
                    x, y = pos[0] + direct[0], pos[1] + direct[1]
                    if (x, y) in obstacleSet:
                        break
                    pos = [x, y]
                    command -= 1

                dist = max(dist, pos[0]**2 + pos[1]**2)

        return dist
