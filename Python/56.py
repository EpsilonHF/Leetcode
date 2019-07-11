"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them 
into [1,6].
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return []

        intervals = sorted(intervals, key = lambda x: x[0])
        ans = [intervals[0]]

        for left, right in intervals[1:]:
            if left > ans[-1][1]:
                ans.append([left, right])
            elif right <= ans[-1][1]:
                continue
            else:
                ans[-1][1] = right

        return ans
