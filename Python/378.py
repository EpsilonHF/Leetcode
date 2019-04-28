"""
Given a n x n matrix where each of the rows and columns are 
sorted in ascending order, find the kth smallest element in 
the matrix.

Note that it is the kth smallest element in the sorted order, 
not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
"""

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        result, heap = None, []
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        while k:
            result, row, col = heapq.heappop(heap)
            if row == 0 and col + 1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
            if row + 1 < len(matrix):
                heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))
            k -= 1

        return result
