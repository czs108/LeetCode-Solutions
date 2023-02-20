# 329. Longest Increasing Path in a Matrix

# Runtime: 483 ms, faster than 71.14% of Python3 online submissions for Longest Increasing Path in a Matrix.

# Memory Usage: 15.1 MB, less than 76.43% of Python3 online submissions for Longest Increasing Path in a Matrix.


class Solution:
    # Depth-first Search
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        lens = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i: int, j: int) -> int:
            if lens[i][j] > 0:
                return lens[i][j]
            for d in dirs:
                new_i, new_j = i + d[0], j + d[1]
                if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]) and matrix[new_i][new_j] > matrix[i][j]:
                    lens[i][j] = max(lens[i][j], dfs(new_i, new_j))
            lens[i][j] += 1
            return lens[i][j]

        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, dfs(i, j))
        return ans