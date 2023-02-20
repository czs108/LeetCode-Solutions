# 1337. The K Weakest Rows in a Matrix

# Runtime: 104 ms, faster than 90.30% of Python3 online submissions for The K Weakest Rows in a Matrix.

# Memory Usage: 14.6 MB, less than 48.08% of Python3 online submissions for The K Weakest Rows in a Matrix.


import heapq

class Solution:
    # Binary Search and Priority Queue
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
            heapq.heappush(heap, (strength, i))

        idxes = []
        while len(idxes) != k:
            _, i = heapq.heappop(heap)
            idxes.append(i)
        return idxes