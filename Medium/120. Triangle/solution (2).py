# 120. Triangle

# Runtime: 110 ms, faster than 9.82% of Python3 online submissions for Triangle.

# Memory Usage: 15.2 MB, less than 46.17% of Python3 online submissions for Triangle.


class Solution:
    # Bottom-up Dynamic Programming (Flip Triangle Upside Down)
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(0, row + 1):
                min_path = min(triangle[row + 1][col], triangle[row + 1][col + 1])
                triangle[row][col] += min_path
        return triangle[0][0]