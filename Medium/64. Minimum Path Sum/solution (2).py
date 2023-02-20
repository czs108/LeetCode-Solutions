# 64. Minimum Path Sum

# 20 / 61 test cases passed.
# Status: Time Limit Exceeded


class Solution:
    # Recursive
    def minPathSum(self, grid: list[list[int]]) -> int:

        def min_path_sum(i: int, j: int) -> int:
            if i == 0 and j == 0:
                return grid[0][0]
            elif i == 0:
                return min_path_sum(i, j - 1) + grid[i][j]
            elif j == 0:
                return min_path_sum(i - 1, j) + grid[i][j]
            else:
                return min(min_path_sum(i - 1, j), min_path_sum(i, j - 1)) + grid[i][j]

        return min_path_sum(len(grid) - 1, len(grid[0]) - 1)