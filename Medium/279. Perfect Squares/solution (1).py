# 279. Perfect Squares

# Runtime: 7508 ms, faster than 5.04% of Python3 online submissions for Perfect Squares.

# Memory Usage: 14.1 MB, less than 48.80% of Python3 online submissions for Perfect Squares.


import math

class Solution:
    # Dynamic Programming
    def numSquares(self, n: int) -> int:
        count = [math.inf for _ in range(n + 1)]
        count[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                count[i] = min(count[i], count[i - j * j] + 1)
                j += 1
        return count[-1]