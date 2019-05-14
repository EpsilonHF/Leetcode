"""
Design your implementation of the linked list. You can choose 
to use the singly linked list or the doubly linked list. A node 
in a singly linked list should have two attributes: val and next. 
val is the value of the current node, and next is a pointer/reference 
to the next node. If you want to use the doubly linked list, 
you will need one more attribute prev to indicate the previous 
node in the linked list. Assume all nodes in the linked list are 
0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. 
If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element 
of the linked list. After the insertion, the new node will be the 
first node of the linked list.
addAtTail(val) : Append a node of value val to the last element 
of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th 
node in the linked list. If index equals to the length of linked 
list, the node will be appended to the end of linked list. If index 
is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, 
if the index is valid.
Example:

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
"""

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = self
        self.pre = self
        self.length = 0

    def _getindex(self, index):

        if index < 0:
            index = self.length + index
        if index >= self.length or index < 0:
            return None

        node = self
        while index + 1:
            node = node.next
            index -= 1

        return node

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. 
        If the index is invalid, return -1.
        """
        if index < 0:
            return -1

        node = self._getindex(index)

        if node:
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the 
        linked list. After the insertion, the new node will be 
        the first node of the linked list.
        """
        node = MyLinkedList()
        node.val = val
        node.next = self.next
        self.next.pre = node
        self.next = node
        node.pre = self
        self.length += 1


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the 
        linked list.
        """
        node = MyLinkedList()
        node.val = val
        node.pre = self.pre
        self.pre.next = node
        node.next = self
        self.pre = node
        self.length += 1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the 
        linked list. If index equals to the length of linked list, 
        the node will be appended to the end of linked list. If 
        index is greater than the length, the node will not be 
        inserted.
        """
        if index == self.length or index == -1:
            self.addAtTail(val)
            return

        if index < 0:
            index = self.length + index

        if index > self.length or index < 0:
            return

        node = MyLinkedList()
        node.val = val

        start = self._getindex(index).pre

        node.next = start.next
        start.next.pre = node
        start.next = node
        node.pre = start

        self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the 
        index is valid.
        """
        if index >= self.length or index < 0:
            return

        start = self._getindex(index).pre

        node = start.next.next
        start.next = node
        node.pre = start

        self.length -= 1
