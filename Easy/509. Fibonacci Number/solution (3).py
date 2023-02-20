# 509. Fibonacci Number

# Runtime: 32 ms, faster than 66.63% of Python3 online submissions for Fibonacci Number.

# Memory Usage: 14.2 MB, less than 41.38% of Python3 online submissions for Fibonacci Number.


class Solution:
    # Top-Down Approach using Memoization
    def __init__(self) -> None:
        self._sums: map[int, int] = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if n in self._sums:
            return self._sums[n]
        else:
            self._sums[n] = self.fib(n - 1) + self.fib(n - 2)
            return self._sums[n]