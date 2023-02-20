# 200. Number of Islands

# Runtime: 403 ms, faster than 30.49% of Python3 online submissions for Number of Islands.

# Memory Usage: 16.7 MB, less than 75.08% of Python3 online submissions for Number of Islands.


class Solution:
    # Breadth First Search
    def numIslands(self, grid: list[list[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1

                    que = [(i, j)]
                    while que:
                        r, c = que.pop()
                        grid[r][c] = '0'
                        if r - 1 >= 0 and grid[r - 1][c] == '1':
                            que.append((r - 1, c))
                        if r + 1 < len(grid) and grid[r + 1][c] == '1':
                            que.append((r + 1, c))
                        if c - 1 >= 0 and grid[r][c - 1] == '1':
                            que.append((r, c - 1))
                        if c + 1 < len(grid[0]) and grid[r][c + 1] == '1':
                            que.append((r, c + 1))
        return count