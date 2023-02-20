# 566. Reshape the Matrix

# Runtime: 115 ms, faster than 28.90% of Python3 online submissions for Reshape the Matrix.

# Memory Usage: 14.8 MB, less than 87.88% of Python3 online submissions for Reshape the Matrix.


class Solution:
    # Using division and modulus
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        if len(mat) == 0 or r * c != len(mat) * len(mat[0]):
            return mat

        res = [[0 for _ in range(c)] for _ in range(r)]
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res[count // c][count % c] = mat[i][j]
                count += 1
        return res