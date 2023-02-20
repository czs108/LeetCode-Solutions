# 1137. N-th Tribonacci Number

# Runtime: 32 ms, faster than 35.84% of Python3 online submissions for N-th Tribonacci Number.

# Memory Usage: 14.3 MB, less than 15.94% of Python3 online submissions for N-th Tribonacci Number.


class Solution:
    # Space Optimisation - Dynamic Programming
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0

        x, y, z = 0, 1, 1
        for _ in range(n - 2):
            x, y, z = y, z, x + y + z
        return z