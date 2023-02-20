# 64. Minimum Path Sum

# Runtime: 92 ms, faster than 97.39% of Python3 online submissions for Minimum Path Sum.

# Memory Usage: 15.5 MB, less than 17.54% of Python3 online submissions for Minimum Path Sum.


class Solution:
    # Dynamic Programming
    def minPathSum(self, grid: list[list[int]]) -> int:
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]