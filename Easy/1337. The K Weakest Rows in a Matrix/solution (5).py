# 1337. The K Weakest Rows in a Matrix

# Runtime: 108 ms, faster than 76.66% of Python3 online submissions for The K Weakest Rows in a Matrix.

# Memory Usage: 14.5 MB, less than 76.31% of Python3 online submissions for The K Weakest Rows in a Matrix.


import heapq

class Solution:
    # Binary Search and Max Priority Queue
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:

        # Find the index of the first 0.
        def calc_sum_by_bin_sec(row: list[int]) -> int:
            low, high = 0, len(row)
            while low < high:
                mid = low + (high - low) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid
            return low

        heap = []
        for i, row in enumerate(mat):
            strength = calc_sum_by_bin_sec(row)
            # Simulate a max priority queue.
            entry = (-strength, -i)
            if len(heap) < k or entry > heap[0]:
                # When we already found k max entries in the queue, which are k weakest rows,
                # then if a new entry is less then the max entry, we do not need to add it.
                # Because the new row is stronger than the current k rows.
                heapq.heappush(heap, entry)
            if len(heap) > k:
                heapq.heappop(heap)

        idxes = []
        while len(idxes) != k:
            _, i = heapq.heappop(heap)
            idxes.append(-i)
        return idxes[::-1]