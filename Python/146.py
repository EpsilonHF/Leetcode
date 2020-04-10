"""
Design and implement a data structure for Least Recently Used (LRU) 
cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the 
key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already 
present. When the cache reached its capacity, it should invalidate the 
least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class Node:

    def __init__(self, key, val):

        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:

        if key in self.dict:
            node = self._remove(self.dict[key])
            self._add(node)
            return node.val

        return -1


    def put(self, key: int, value: int) -> None:

        if key in self.dict:
            self._remove(self.dict[key])

        node = Node(key, value)
        self._add(node)
        self.dict[key] = node

        if len(self.dict) > self.capacity:
            last = self.tail.prev
            self._remove(last)
            del self.dict[last.key]


    def _remove(self, node):

        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

        return node


    def _add(self, node):

        n = self.head.next
        node.prev = self.head
        node.next = n
        n.prev = node
        self.head.next = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
