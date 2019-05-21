"""
In a row of seats, 1 represents a person sitting in that seat,
and 0 represents that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between 
him and the closest person to him is maximized.

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest 
person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
"""

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l1 = dist = pre = first = 0

        for i, s in enumerate(seats):
            if s:
                dist = max(i - pre, dist)
                pre = i

                if not first:
                    l1 = i
                    first = 1

        l3 = len(seats) - pre - 1

        return max(l1, dist//2, l3)
