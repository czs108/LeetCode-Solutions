# 1337. The K Weakest Rows in a Matrix

# Runtime: 108 ms, faster than 76.66% of Python3 online submissions for The K Weakest Rows in a Matrix.

# Memory Usage: 14.7 MB, less than 16.17% of Python3 online submissions for The K Weakest Rows in a Matrix.


class Solution:
    # Binary Search and Sorting
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


        strengths = []
        for i, row in enumerate(mat):
            strengths.append((calc_sum_by_bin_sec(row), i))

        strengths.sort()

        idxes = []
        for i in range(k):
            idxes.append(strengths[i][1])
        return idxes