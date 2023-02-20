# 1314. Matrix Block Sum

# Runtime: 248 ms, faster than 26.09% of Python3 online submissions for Matrix Block Sum.

# Memory Usage: 15.5 MB, less than 40.49% of Python3 online submissions for Matrix Block Sum.


class Solution:
    # Dynamic Programming | Prefix Sum
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        sum = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]
        for row in range(1, len(mat) + 1):
            for col in range(1, len(mat[0]) + 1):
                sum[row][col] = sum[row - 1][col] + sum[row][col - 1] - sum[row - 1][col - 1] + mat[row - 1][col - 1]

        def get_sum(row: int, col: int) -> int:
            row = max(min(row, len(sum) - 1), 0)
            col = max(min(col, len(sum[0]) - 1), 0)
            return sum[row][col]

        res = [[0] * (len(mat[0])) for _ in range(len(mat))]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                res[row][col] = get_sum(row + k + 1, col + k + 1) - get_sum(row - k, col + k + 1) - get_sum(row + k + 1, col - k) + get_sum(row - k, col - k)
        return res