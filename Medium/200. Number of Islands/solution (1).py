# 200. Number of Islands

# Runtime: 333 ms, faster than 49.77% of Python3 online submissions for Number of Islands.

# Memory Usage: 17 MB, less than 34.26% of Python3 online submissions for Number of Islands.


class Solution:
    # Depth First Search
    def numIslands(self, grid: list[list[str]]) -> int:

        def dfs(r: int, c: int) -> None:
            grid[r][c] = '0'
            if r - 1 >= 0 and grid[r - 1][c] == '1':
                dfs(r - 1, c)
            if r + 1 < len(grid) and grid[r + 1][c] == '1':
                dfs(r + 1, c)
            if c - 1 >= 0 and grid[r][c - 1] == '1':
                dfs(r, c - 1)
            if c + 1 < len(grid[0]) and grid[r][c + 1] == '1':
                dfs(r, c + 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count