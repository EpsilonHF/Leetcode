"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), 
the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        s = s.strip()
        num = 0
        n = 0
        char = set("()+-")

        for ch in s[::-1]:
            if ch.isdigit():
                num += int(ch) * (10 ** n)
                n += 1

            elif ch != " ":
                if n:
                    stack.append(num)
                    num = n = 0
                if ch == "(":
                    res = self.evaluate(stack)
                    stack.pop()
                    stack.append(res)
                else:
                    stack.append(ch)

        if n:
            stack.append(num)

        return self.evaluate(stack)



    def evaluate(self, stack):

        res = stack.pop() if stack else 0

        while stack and stack[-1] != ")":
            sign = stack.pop()
            if sign == "+":
                res += stack.pop()
            else:
                res -= stack.pop()

        return res

