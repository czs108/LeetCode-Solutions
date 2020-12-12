# 1137. N-th Tribonacci Number

# Runtime: 32 ms, faster than 35.84% of Python3 online submissions for N-th Tribonacci Number.

# Memory Usage: 14.3 MB, less than 15.94% of Python3 online submissions for N-th Tribonacci Number.


class Solution:
    _MAX_IDX: int = 38

    # Performance Optimisation - Dynamic Programming
    def __init__(self):
        self._nums = [0] * self._MAX_IDX
        self._nums[1] = self._nums[2] = 1
        for i in range(3, self._MAX_IDX):
            self._nums[i] = self._nums[i - 1] + self._nums[i - 2] + self._nums[i - 3]

    def tribonacci(self, n: int) -> int:
        return self._nums[n]