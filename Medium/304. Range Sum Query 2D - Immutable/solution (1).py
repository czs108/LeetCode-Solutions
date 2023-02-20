# 304. Range Sum Query 2D - Immutable

# Runtime: 2122 ms, faster than 28.89% of Python3 online submissions for Range Sum Query 2D - Immutable.

# Memory Usage: 24.8 MB, less than 48.16% of Python3 online submissions for Range Sum Query 2D - Immutable.


class NumMatrix:
    # Dynamic Programming | Prefix Sum
    def __init__(self, matrix: list[list[int]]) -> None:
        self._sum: list[list[int]] = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for row in range(1, len(matrix) + 1):
            for col in range(1, len(matrix[0]) + 1):
                self._sum[row][col] = self._sum[row - 1][col] + self._sum[row][col - 1] - self._sum[row - 1][col - 1] + matrix[row - 1][col - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self._get_sum(row2 + 1, col2 + 1) - self._get_sum(row2 + 1, col1) - self._get_sum(row1, col2 + 1) + self._get_sum(row1, col1)

    def _get_sum(self, row: int, col: int) -> int:
        row = max(min(row, len(self._sum) - 1), 0)
        col = max(min(col, len(self._sum[0]) - 1), 0)
        return self._sum[row][col]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1, col1, row2, col2)