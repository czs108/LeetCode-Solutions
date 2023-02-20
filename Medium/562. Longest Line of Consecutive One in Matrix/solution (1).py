# 562. Longest Line of Consecutive One in Matrix

# Runtime: 511 ms, faster than 60.17% of Python3 online submissions for Longest Line of Consecutive One in Matrix.

# Memory Usage: 17.4 MB, less than 56.00% of Python3 online submissions for Longest Line of Consecutive One in Matrix.


class Solution:
    # Dynamic Programming
    def longestLine(self, mat: list[list[int]]) -> int:
        Hrz, Vrt, Dgn, AntiDgn = 0, 1, 2, 3
        max_count = 0
        counts = [[[0] * 4 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    continue
                counts[i][j][Hrz] = counts[i][j - 1][Hrz] + 1 if j > 0 else 1
                counts[i][j][Vrt] = counts[i - 1][j][Vrt] + 1 if i > 0 else 1
                counts[i][j][Dgn] = counts[i - 1][j - 1][Dgn] + 1 if i > 0 and j > 0 else 1
                counts[i][j][AntiDgn] = counts[i - 1][j + 1][AntiDgn] + 1 if i > 0 and j < len(mat[0]) - 1 else 1
                max_count = max(max_count, counts[i][j][Hrz], counts[i][j][Vrt], counts[i][j][Dgn], counts[i][j][AntiDgn])
        return max_count