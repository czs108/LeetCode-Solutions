# 378. K-th Smallest Element in a Sorted Matrix


import heapq

class Solution:
    # Min-Heap
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        N = len(matrix)

        min_heap = []
        for row in range(min(N, k)):
            # Store (value, row, column).
            min_heap.append((matrix[row][0], row, 0))

        heapq.heapify(min_heap)

        while k:
            val, row, col = heapq.heappop(min_heap)
            if col < N - 1:
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
            k -= 1

        return val