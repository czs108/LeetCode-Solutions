# 64. Minimum Path Sum

# 20 / 61 test cases passed.
# Status: Time Limit Exceeded


class Solution:
    # Recursive
    def minPathSum(self, grid: List[List[int]]) -> int:
        return Solution._minPathSum(grid, len(grid) - 1, len(grid[0]) - 1)

    @staticmethod
    def _minPathSum(grid: List[List[int]], i: int, j: int) -> int:
        if i == 0 and j == 0:
            return grid[0][0]
        elif i == 0:
            return Solution._minPathSum(grid, i, j - 1) + grid[i][j]
        elif j == 0:
            return Solution._minPathSum(grid, i - 1, j) + grid[i][j]
        else:
            return min(Solution._minPathSum(grid, i - 1, j), Solution._minPathSum(grid, i, j - 1)) + grid[i][j]