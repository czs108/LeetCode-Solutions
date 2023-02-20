# 695. Max Area of Island

# Runtime: 144 ms, faster than 62.66% of Python3 online submissions for Max Area of Island.

# Memory Usage: 14.5 MB, less than 92.26% of Python3 online submissions for Max Area of Island.


class Solution:
    # Depth-First Search
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited = set()

        def dfs(sr: int, sc: int) -> int:
            if (sr, sc) in visited or grid[sr][sc] == 0:
                return 0

            stack = [(sr, sc)]
            visited.add((sr, sc))

            size = 0
            while stack:
                r, c = stack.pop(-1)
                size += 1

                if r >= 1 and grid[r - 1][c] == 1 and (r - 1, c) not in visited:
                    stack.append((r - 1, c))
                    visited.add((r - 1, c))
                if r + 1 < len(grid) and grid[r + 1][c] == 1 and (r + 1, c) not in visited:
                    stack.append((r + 1, c))
                    visited.add((r + 1, c))
                if c >= 1 and grid[r][c - 1] == 1 and (r, c - 1) not in visited:
                    stack.append((r, c - 1))
                    visited.add((r, c - 1))
                if c + 1 < len(grid[0]) and grid[r][c + 1] == 1 and (r, c + 1) not in visited:
                    stack.append((r, c + 1))
                    visited.add((r, c + 1))
            return size

        max_size = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_size = max(max_size, dfs(i, j))
        return max_size