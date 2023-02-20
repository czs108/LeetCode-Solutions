# 1337. The K Weakest Rows in a Matrix

# Runtime: 112 ms, faster than 54.72% of Python3 online submissions for The K Weakest Rows in a Matrix.

# Memory Usage: 14.6 MB, less than 48.08% of Python3 online submissions for The K Weakest Rows in a Matrix.


class Solution:
    # Linear Search and Sorting
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        strengths = []
        for i, row in enumerate(mat):
            strengths.append((sum(row), i))

        strengths.sort()

        idxes = []
        for i in range(k):
            idxes.append(strengths[i][1])
        return idxes