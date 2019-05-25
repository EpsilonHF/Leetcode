"""
We have a collection of rocks, each rock has a positive integer 
weight.

Each turn, we choose the two heaviest rocks and smash them together.  
Suppose the stones have weights x and y with x <= y. The result 
of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the 
stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of 
this stone (or 0 if there are no stones left.)

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then 
that's the value of last stone.
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            lst = []
            if stones[0] > stones[1]:
                two = [stones[0], stones[1]]
            else:
                two = [stones[1], stones[0]]

            for i in range(2, len(stones)):
                if stones[i] > two[0]:
                    lst.append(two[1])
                    two = [stones[i], two[0]]
                elif stones[i] > two[1]:
                    lst.append(two[1])
                    two = [two[0], stones[i]]
                else:
                    lst.append(stones[i])
            if two[0] != two[1]:
                lst.append(two[0] - two[1])

            stones = lst

        return stones[0] if len(stones) else 0
