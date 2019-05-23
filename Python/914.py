"""
n a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it 
is possible to split the entire deck into 1 or more groups of 
cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.

Example 1:

Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
"""

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = dict()
        for card in deck:
            d[card] = d.get(card, 0) + 1

        if min(d.values()) < 2:
            return False

        N = len(deck) // len(set(deck))

        for i in range(2, N+1):
            ret = True
            for key in d:
                if d[key] % i:
                    ret = False
                    break

            if ret:
                return True

        return False
