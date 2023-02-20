# 48. Rotate image

# Runtime: 36 ms, faster than 68.92% of Python3 online submissions for Rotate Image.

# Memory Usage: 14.4 MB, less than 28.18% of Python3 online submissions for Rotate Image.


class Solution:
    # Rotate Groups of Four Cells
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for r in range(n // 2 + n % 2):
            for c in range(n // 2):
                tmp = matrix[n - 1 - c][r]
                matrix[n - 1 - c][r] = matrix[n - 1 - r][n - c - 1]
                matrix[n - 1 - r][n - c - 1] = matrix[c][n - 1 -r]
                matrix[c][n - 1 - r] = matrix[r][c]
                matrix[r][c] = tmp