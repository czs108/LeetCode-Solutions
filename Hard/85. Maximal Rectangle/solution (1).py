# 85. Maximal Rectangle

# Runtime: 2500 ms, faster than 5.04% of Python3 online submissions for Maximal Rectangle.

# Memory Usage: 15.2 MB, less than 96.86% of Python3 online submissions for Maximal Rectangle.


class Solution:
    # Dynamic Programming on Histograms
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        max_area = 0
        max_width = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    continue

                # Compute the maximum width.
                max_width[i][j] = max_width[i][j - 1] + 1 if j > 0 else 1

                # Compute the maximum area rectangle with a lower right corner at [i, j].
                width = max_width[i][j]
                for k in range(i, -1, -1):
                    width = min(width, max_width[k][j])
                    max_area = max(max_area, width * (i - k + 1))

        return max_area