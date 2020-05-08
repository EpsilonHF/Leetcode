"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another 
expression.

Note:
Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would 
always evaluate to a result and there won't be any divide by zero operation.

Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        lst = []

        for token in tokens:

            if token.isdigit() or token[1:].isdigit():
                lst.append(int(token))
                continue

            var1 = lst.pop()
            var2 = lst.pop()

            if token == "+":
                var = var1 + var2
            if token == "-":
                var = var2 - var1
            if token == "*":
                var = var1 * var2
            if token == "/":
                var = int(var2 / var1)

            lst.append(var)

        return lst[0]
       
