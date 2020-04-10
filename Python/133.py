"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) 
of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


Test case format:

For simplicity sake, each node's value is the same as the node's 
index (1-indexed). For example, the first node with val = 1, the second 
node with val = 2, and so on. The graph is represented in the test case 
using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a 
finite graph. Each list describes the set of neighbors of a node in the 
graph.

The given node will always be the first node with val = 1. You must return 
the copy of the given node as a reference to the cloned graph.


Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if node is None:
            return None

        node_map = dict()

        lst = [node]

        while lst:
            point = lst[0]
            node_map[point] = Node(point.val, [])

            for i in point.neighbors:
                if i in node_map:
                    continue
                node_map[i] = Node(i.val, [])
                lst.append(i)

            lst.pop(0)

        lst = [node]
        record = set()

        while lst:
            point = lst[0]
            node_map[point].neighbors = [node_map[node] for node in point.neighbors]

            for i in point.neighbors:
                if i in record:
                    continue
                record.add(i)
                lst.append(i)

            lst.pop(0)

        return node_map[node]


