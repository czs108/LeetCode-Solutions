# 542. 01 Matrix


import math

class Solution:
    # BFS
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        dist = [[math.inf] * len(mat[0]) for _ in range(len(mat))]
        que = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    dist[row][col] = 0
                    que.append((row, col))

        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        while que:
            row, col = que.pop()
            for dir in dirs:
                next_row, next_col = row + dir[0], col + dir[1]
                if 0 <= next_row and next_row < len(mat) and 0 <= next_col and next_col < len(mat[0]):
                    if dist[next_row][next_col] > dist[row][col] + 1:
                        dist[next_row][next_col] = dist[row][col] + 1
                        que.append((next_row, next_col))
        return dist