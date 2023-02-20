# 509. Fibonacci Number

# Runtime: 28 ms, faster than 85.55% of Python3 online submissions for Fibonacci Number.

# Memory Usage: 14.2 MB, less than 41.38% of Python3 online submissions for Fibonacci Number.


class Solution:
    # Iterative Bottom-Up Approach
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            curr = 0
            prev1, prev2 = 1, 0
            for i in range(2, n + 1):
                curr = prev1 + prev2
                prev1, prev2 = curr, prev1
            return curr