# 120. Triangle

# Runtime: 120 ms, faster than 6.00% of Python3 online submissions for Triangle.

# Memory Usage: 15.1 MB, less than 69.83% of Python3 online submissions for Triangle.


import math

class Solution:
    # Bottom-up Dynamic Programming (In-place)
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for row in range(1, len(triangle)):
            for col in range(row + 1):
                min_path = math.inf
                if col > 0:
                    min_path = min(triangle[row - 1][col - 1], min_path)
                if col < row:
                    min_path = min(triangle[row - 1][col], min_path)
                triangle[row][col] += min_path
        return min(triangle[-1])