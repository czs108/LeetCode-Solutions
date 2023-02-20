# 542. 01 Matrix

# Runtime: 632 ms, faster than 74.73% of Python3 online submissions for 01 Matrix.

# Memory Usage: 17.3 MB, less than 58.87% of Python3 online submissions for 01 Matrix.


import math

class Solution:
    # Dynamic Programming
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        dist = [[math.inf] * len(mat[0]) for _ in range(len(mat))]

        # First pass: check for left and top.
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    dist[row][col] = 0
                else:
                    if row > 0:
                        dist[row][col] = min(dist[row][col], dist[row - 1][col] + 1)
                    if col > 0:
                        dist[row][col] = min(dist[row][col], dist[row][col - 1] + 1)

        # Second pass: check for bottom and right.
        for row in range(len(mat) - 1, -1, -1):
            for col in range(len(mat[0]) - 1, -1, -1):
                if row < len(mat) - 1:
                    dist[row][col] = min(dist[row][col], dist[row + 1][col] + 1)
                if col < len(mat[0]) - 1:
                    dist[row][col] = min(dist[row][col], dist[row][col + 1] + 1)

        return dist