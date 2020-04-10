"""
A linked list is given such that each node contains an additional random 
pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random 
pointer points to, or null if it does not point to any node.


Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if head is None:
            return None

        node_map = dict()

        node = head

        while node:
            new_node = Node(node.val)
            node_map[node] = new_node
            node = node.next

        node = head

        while node:
            if node.next:
                node_map[node].next = node_map[node.next]
            if node.random:
                node_map[node].random = node_map[node.random]
            node = node.next

        return node_map[head]
