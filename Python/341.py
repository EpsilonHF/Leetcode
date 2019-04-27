"""
Given a nested list of integers, implement an iterator to 
flatten it.

Each element is either an integer, or a list -- whose elements 
may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: 
By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,1,2,1,1].
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.data = []
        def init(lst):
            for element in lst:
                if element.isInteger():
                    self.data.append(element.getInteger())
                else:
                    init(element.getList())

        init(nestedList)
        self.data = self.data[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.data.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.data) > 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
