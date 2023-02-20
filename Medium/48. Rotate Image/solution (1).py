# 48. Rotate Image

# Runtime: 36 ms, faster than 68.92% of Python3 online submissions for Rotate Image.

# Memory Usage: 14.1 MB, less than 95.35% of Python3 online submissions for Rotate Image.


class Solution:
    # Reverse on Diagonal and then Reverse Left to Right
    def rotate(self, matrix: list[list[int]]) -> None:

        def transpose() -> None:
            for i in range(len(matrix)):
                for j in range(i, len(matrix)):
                    matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        def reflect() -> None:
            for i in range(len(matrix)):
                for j in range(len(matrix) // 2):
                    matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

        transpose()
        reflect()