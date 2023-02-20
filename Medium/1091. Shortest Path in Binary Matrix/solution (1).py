# 1091. Shortest Path in Binary Matrix

# Runtime: 752 ms, faster than 56.15% of Python3 online submissions for Shortest Path in Binary Matrix.

# Memory Usage: 14.7 MB, less than 78.38% of Python3 online submissions for Shortest Path in Binary Matrix.


class Solution:
    # Breadth-first Search
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def neighbours(i: int, j: int) -> Iterable[tuple[int, int]]:
            for dir in dirs:
                next_i, next_j = i + dir[0], j + dir[1]
                if not (0 <= next_i < len(grid) and 0 <= next_j < len(grid[0])):
                    continue
                elif grid[next_i][next_j] != 0:
                    continue
                else:
                    yield next_i, next_j

        que = [(0, 0)]
        grid[0][0] = 1
        while que:
            i, j = que.pop(0)
            dist = grid[i][j]
            if (i, j) == (len(grid) - 1, len(grid[0]) - 1):
                return dist
            else:
                for next_i, next_j in neighbours(i, j):
                    grid[next_i][next_j] = dist + 1
                    que.append((next_i, next_j))
        return -1