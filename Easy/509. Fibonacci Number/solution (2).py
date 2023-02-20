# 509. Fibonacci Number

# Runtime: 24 ms, faster than 95.67% of Python3 online submissions for Fibonacci Number.

# Memory Usage: 14.3 MB, less than 41.38% of Python3 online submissions for Fibonacci Number.


class Solution:
    # Bottom-Up Approach using Tabulation
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            sums = [0 for _ in range(n + 1)]
            sums[1] = 1
            for i in range(2, n + 1):
                sums[i] = sums[i - 1] + sums[i - 2]
            return sums[-1]