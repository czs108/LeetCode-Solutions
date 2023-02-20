# 931. Minimum Falling Path Sum

# Runtime: 116 ms, faster than 77.57% of Python3 online submissions for Minimum Falling Path Sum.

# Memory Usage: 15.4 MB, less than 28.70% of Python3 online submissions for Minimum Falling Path Sum.


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                min_path = matrix[row - 1][col]
                if col > 0:
                    min_path = min(min_path, matrix[row - 1][col - 1])
                if col < len(matrix[0]) - 1:
                    min_path = min(min_path, matrix[row - 1][col + 1])
                matrix[row][col] += min_path
        return min(matrix[-1])