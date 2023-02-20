# 1137. N-th Tribonacci Number

# Runtime: 32 ms, faster than 35.84% of Python3 online submissions for N-th Tribonacci Number.

# Memory Usage: 14.2 MB, less than 40.51% of Python3 online submissions for N-th Tribonacci Number.


class Solution:
    _MAX_IDX: int = 38

    # Performance Optimisation - Recursion with Memoization
    def __init__(self):
        self._nums = [0] * self._MAX_IDX
        self._nums[1] = self._nums[2] = 1
        self._calc(self._MAX_IDX - 1)

    def tribonacci(self, n: int) -> int:
        return self._nums[n]

    def _calc(self, n: int) -> None:
        if n == 0:
            return 0
        elif self._nums[n]:
            return self._nums[n]
        else:
            self._nums[n] = self._calc(n - 1) + self._calc(n - 2) + self._calc(n - 3)
            return self._nums[n]