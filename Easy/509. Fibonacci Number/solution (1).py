# 509. Fibonacci Number

# Runtime: 932 ms, faster than 11.41% of Python3 online submissions for Fibonacci Number.

# Memory Usage: 14.2 MB, less than 70.39% of Python3 online submissions for Fibonacci Number.


class Solution:
    # Recursion
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)