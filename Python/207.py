"""
There are a total of numCourses courses you have to take, labeled from 
0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you 
have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is 
it possible for you to finish all courses?

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: 
There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]

        for x, y in prerequisites:
            graph[x].append(y)

        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False

        return True

    def dfs(self, graph, visited, i):

        if visited[i] == -1:
            return False

        if visited[i] == 1:
            return True

        visited[i] = -1

        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False

        visited[i] = 1

        return True
