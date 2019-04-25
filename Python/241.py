"""
Given a string of numbers and operators, return all possible 
results from computing all the different possible ways to 
group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
"""

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "+-*":
                val1 = self.diffWaysToCompute(input[:i])
                val2 = self.diffWaysToCompute(input[i+1:])
                if input[i] == '+': op = operator.add
                elif input[i] == '-': op = operator.sub
                else: op = operator.mul
                res += [op(i, j) for i in val1 for j in val2]

        return res
