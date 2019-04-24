"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
"""

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.deque()
        self.length = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        self.length += 1


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """

        self.length -= 1
        for i in range(self.length):
            self.data.append(self.data.popleft())

        return self.data.popleft()



    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.data[-1]


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.length == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
