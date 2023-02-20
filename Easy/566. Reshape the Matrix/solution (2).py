# 566. Reshape the Matrix

# Runtime: 182 ms, faster than 5.04% of Python3 online submissions for Reshape the Matrix.

# Memory Usage: 14.7 MB, less than 95.87% of Python3 online submissions for Reshape the Matrix.


class Solution:
    # Without Using Extra Space
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        if len(mat) == 0 or r * c != len(mat) * len(mat[0]):
            return mat

        res = [[0 for _ in range(c)] for _ in range(r)]
        row, col = 0, 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res[row][col] = mat[i][j]
                col += 1
                if col == c:
                    col = 0
                    row += 1
        return res