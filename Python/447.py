"""
Given n points in the plane that are all pairwise distinct, 
a "boomerang" is a tuple of points (i, j, k) such that the 
distance between i and j equals the distance between i and k 
(the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be 
at most 500 and coordinates of points are all in the range 
[-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):
            dist = dict()
            for point in points[:i] + points[i+1:]:
                d = (point[0] - points[i][0]) ** 2 + \
                    (point[1] - points[i][1]) ** 2
                dist[d] = dist.get(d, 0) + 1
            for d in dist:
                res += dist[d] * (dist[d] - 1)

        return res
