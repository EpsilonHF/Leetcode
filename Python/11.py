"""
Given n non-negative integers a1, a2, ..., an , where each 
represents a point at coordinate (i, ai). n vertical lines 
are drawn such that the two endpoints of line i is at (i, ai) 
and (i, 0). Find two lines, which together with x-axis forms 
a container, such that the container contains the most water.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        num = 0
        start = 0
        end = len(height) - 1

        while end != start:
            num = max(num, min(height[start], height[end]) * (end-start))
            if height[end] < height[start]:
                end -= 1
            else:
                start += 1

        return num
