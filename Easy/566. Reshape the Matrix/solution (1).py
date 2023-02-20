# 566. Reshape the Matrix

# Runtime: 109 ms, faster than 30.83% of Python3 online submissions for Reshape the Matrix.

# Memory Usage: 14.7 MB, less than 87.88% of Python3 online submissions for Reshape the Matrix.


class Solution:
    # Using Queue
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        if len(mat) == 0 or r * c != len(mat) * len(mat[0]):
            return mat

        nums = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                nums.append(mat[i][j])

        res = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                res[i][j] = nums.pop(0)
        return res