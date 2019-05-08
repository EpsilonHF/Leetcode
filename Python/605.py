"""
Suppose you have a long flowerbed in which some of the plots are 
planted and some are not. However, flowers cannot be planted in 
adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, 
where 0 means empty and 1 means not empty), and a number n, return 
if n new flowers can be planted in it without violating the 
no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = num = 0

        for f in [0] + flowerbed:
            if f:
                num += (count - 1) // 2
                count = 0
            else:
                count += 1

        if count > 1:
            num += count // 2

        return n <= num
